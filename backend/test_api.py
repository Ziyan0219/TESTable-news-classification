#!/usr/bin/env python3
"""
Testing Tool API - Standalone Classification Testing
Provides identical classification results as the main dashboard for testing purposes
Does NOT save to database - pure testing environment
"""

import os
import sys
import json
import time
import pandas as pd
from pathlib import Path
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import shutil

# Add testing-tool directory to path to import classification modules
testing_tool_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(testing_tool_root)

# Change to testing-tool root directory so relative paths work
original_cwd = os.getcwd()
os.chdir(testing_tool_root)

# Import the SAME classification pipeline used by main dashboard
from archive_classifier_final import pipeline, read_stories

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
UPLOAD_FOLDER = Path('/tmp/test_classification_uploads')
ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'csv'}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def clean_value(val):
    """Clean pandas NaN and None values to prevent N/A display"""
    if pd.isna(val) or val is None:
        return ''
    val_str = str(val).strip()
    # Handle string representations of None/NaN
    if val_str.lower() in ['nan', 'none', '']:
        return ''
    return val_str

def format_confidence_scores(scores_dict):
    """Format confidence scores as readable text"""
    if not scores_dict:
        return ""

    formatted = []
    for place, score in scores_dict.items():
        percentage = int(score * 100)
        formatted.append(f"{place}: {percentage}%")

    return ", ".join(formatted)

def classify_stories(stories_data):
    """
    Run classification using the EXACT SAME pipeline as main dashboard

    Args:
        stories_data: List of URLs or DataFrame with Story column

    Returns:
        List of classification results
    """
    # Ensure upload directory exists
    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    # Create temporary CSV with stories
    temp_dir = UPLOAD_FOLDER / f"test_{int(time.time())}"
    temp_dir.mkdir(parents=True, exist_ok=True)

    temp_csv = temp_dir / 'test_stories.csv'

    # Prepare DataFrame
    if isinstance(stories_data, list):
        # List of URLs
        df = pd.DataFrame({
            'Story': stories_data,
            'Umbrella': '',
            'GeographicArea': '',
            'Neighborhoods': '',
            'SocialAbstract': ''
        })
    else:
        # Already a DataFrame
        df = stories_data

    df.to_csv(temp_csv, index=False)

    # Set up paths (now within testing-tool directory)
    neigh_path = Path(os.path.join(os.path.dirname(__file__), '..', 'Pittsburgh neighborhoods.xlsx'))
    muni_path = Path(os.path.join(os.path.dirname(__file__), '..', 'Allegheny County Municipalities.xlsx'))
    output_dir = temp_dir / 'output'

    # Get API key (optional, teaser generation disabled)
    api_key = os.environ.get('OPENAI_API_KEY')

    try:
        # Run the EXACT SAME pipeline as main dashboard
        start_time = time.time()
        print(f"\n=== DEBUG: Starting classification ===")
        print(f"Input CSV: {temp_csv}")
        print(f"Neigh path: {neigh_path}, exists: {neigh_path.exists()}")
        print(f"Muni path: {muni_path}, exists: {muni_path.exists()}")
        print(f"Output dir: {output_dir}")

        pipeline(temp_csv, neigh_path, muni_path, output_dir, api_key)
        processing_time = time.time() - start_time

        print(f"=== DEBUG: Classification completed in {processing_time:.1f}s ===\n")

        # Read results
        result_file = output_dir / 'stories_classified_filled.csv'
        confidence_file = output_dir / 'confidence_analysis.json'

        if not result_file.exists():
            raise Exception("Classification failed - no result file generated")

        df_results = pd.read_csv(result_file)

        print(f"=== DEBUG: Results loaded ===")
        print(f"Columns: {df_results.columns.tolist()}")
        if len(df_results) > 0:
            print(f"First row Umbrella: {df_results.iloc[0]['Umbrella']}")
            print(f"First row GeographicArea: {df_results.iloc[0]['GeographicArea']}")
            print(f"First row Neighborhoods: {df_results.iloc[0]['Neighborhoods']}")

        # Load confidence scores
        confidence_data = {}
        if confidence_file.exists():
            with open(confidence_file, 'r', encoding='utf-8') as f:
                conf_json = json.load(f)
                confidence_data = conf_json.get('story_confidence_scores', [])
                print(f"Confidence scores loaded: {len(confidence_data)} stories")
                if confidence_data and len(confidence_data) > 0:
                    print(f"First story confidence: {confidence_data[0]}")

        # Format results
        results = []
        for idx, row in df_results.iterrows():
            # Get confidence scores for this story
            story_confidence = confidence_data[idx] if idx < len(confidence_data) else {}

            result = {
                'url': clean_value(row.get('Story', '')),
                'title': clean_value(row.get('Title', '')),
                'author': clean_value(row.get('Author', '')),
                'date': clean_value(row.get('Date', '')),
                'umbrella': clean_value(row.get('Umbrella', '')),
                'geographic_area': clean_value(row.get('GeographicArea', '')),
                'neighborhoods': clean_value(row.get('Neighborhoods', '')),
                'confidence_scores': story_confidence,
                'confidence_text': format_confidence_scores(story_confidence),
                'processing_time': f"{processing_time / len(df_results):.1f}s"
            }
            results.append(result)

        # Cleanup temp files
        shutil.rmtree(temp_dir, ignore_errors=True)

        return {
            'success': True,
            'results': results,
            'total_processing_time': f"{processing_time:.1f}s",
            'total_articles': len(results)
        }

    except Exception as e:
        # Cleanup on error
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise e

@app.route('/api/test-classify', methods=['POST'])
def test_classify():
    """
    Main endpoint for classification testing
    Accepts: Single URL (JSON) or Excel file upload
    Returns: Formatted classification results
    """
    try:
        # Check if it's a file upload
        if 'file' in request.files:
            file = request.files['file']

            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400

            if not allowed_file(file.filename):
                return jsonify({'error': 'Invalid file format. Please upload Excel or CSV file.'}), 400

            # Save uploaded file
            UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
            filename = secure_filename(file.filename)
            filepath = UPLOAD_FOLDER / filename
            file.save(str(filepath))

            # Read stories from Excel/CSV
            try:
                if filepath.suffix.lower() in ['.xls', '.xlsx']:
                    df = pd.read_excel(filepath, engine='openpyxl')
                else:
                    df = pd.read_csv(filepath)

                # Ensure Story column exists
                if 'Story' not in df.columns:
                    return jsonify({'error': 'Excel file must contain a "Story" column with URLs'}), 400

                # Run classification
                result = classify_stories(df)

                # Cleanup uploaded file
                filepath.unlink()

                return jsonify(result)

            except Exception as e:
                filepath.unlink(missing_ok=True)
                return jsonify({'error': f'Error processing file: {str(e)}'}), 500

        # Check if it's a JSON request with single URL
        elif request.is_json:
            data = request.get_json()
            url = data.get('url', '').strip()

            if not url:
                return jsonify({'error': 'Please provide a URL'}), 400

            if not url.startswith('http'):
                return jsonify({'error': 'Invalid URL. Must start with http:// or https://'}), 400

            # Run classification for single URL
            result = classify_stories([url])

            return jsonify(result)

        else:
            return jsonify({'error': 'Invalid request. Send JSON with URL or upload Excel file.'}), 400

    except Exception as e:
        app.logger.error(f"Classification error: {str(e)}")
        return jsonify({'error': f'Classification failed: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Classification Testing Tool',
        'version': '1.0'
    })

@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API information"""
    return jsonify({
        'service': 'PublicSource Classification Testing Tool',
        'version': '1.0',
        'endpoints': {
            '/api/test-classify': 'POST - Test classification (single URL or Excel file)',
            '/api/health': 'GET - Health check'
        },
        'usage': {
            'single_url': 'POST JSON: {"url": "https://..."}',
            'excel_upload': 'POST multipart/form-data with "file" field'
        }
    })

if __name__ == '__main__':
    # Support both local development (port 5001) and Hugging Face Spaces (port 7860)
    port = int(os.environ.get('PORT', 5001))

    print("=" * 60)
    print("PublicSource Classification Testing Tool")
    print("=" * 60)
    print(f"Starting server on http://0.0.0.0:{port}")
    print(f"Using SAME classification logic as main dashboard")
    print(f"Test mode: Results NOT saved to database")
    print("=" * 60)

    app.run(host='0.0.0.0', port=port, debug=False)
