# PublicSource Classification Testing Tool

[![Demo](https://img.shields.io/badge/Demo-Live-brightgreen)](https://testable-news-classification.vercel.app)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)

A standalone testing platform for article classification that provides real-time geographic classification results without saving to database.

## 🎯 Features

- ✅ **Identical classification logic as main dashboard**
- ✅ **Single URL and Excel batch testing**
- ✅ **Real-time formatted text results**
- ✅ **Pure testing environment (no database saving)**
- ✅ **Non-technical user-friendly interface**
- ✅ **Advanced NLP-based geographic classification**

## 🚀 Quick Start

### Option 1: Local Deployment

#### Requirements
- Python 3.11+
- Flask, pandas, openpyxl
- All dependencies from main project

#### Start Backend
```bash
cd backend
python test_api.py
```

#### Open Frontend
Simply open `frontend/index.html` in your browser, or:
```bash
cd frontend
python -m http.server 8080
```
Then visit: http://localhost:8080

### Option 2: Online Demo

Visit the live demo: **[TESTable Classification Tool](https://testable-news-classification.vercel.app)**

⚠️ **Important Note for Online Demo:**
- The online frontend is hosted on Vercel
- Backend API **must be self-hosted** locally (cannot be deployed to Vercel)
- Configure your local backend URL in the frontend settings

## 📖 Usage

### Test Single URL

1. Paste article URL in the input box
2. Click "Test" button
3. Wait for results (typically 2-5 seconds)

Example URL:
```
https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
```

### Batch Test Excel

1. Prepare Excel file (.xlsx, .xls, or .csv)
2. Ensure it has a `Story` column with article URLs
3. Drag & drop file to upload area or click to select
4. Results will display for all articles

### Copy and Clear

- **Copy**: Click "📋 Copy" to copy all results to clipboard
- **Clear**: Click "🗑️ Clear" to remove displayed results

## 📊 Classification Results

Each article returns:

- 📰 **Title** - Article headline
- ✍️ **Author** - Article author
- 📅 **Date** - Publication date
- 🏠 **Umbrella** - Top-level classification
  - `Pittsburgh` - Within Pittsburgh city
  - `Allegheny County` - Outside Pittsburgh, within county
  - `Pittsburgh, Allegheny County` - Covers both
- 📍 **Geographic Area** - Mid-level region
  - For Pittsburgh neighborhoods: `North Side`, `East End`, `South Pittsburgh`, etc.
  - For municipalities: `Northwest suburbs`, `Mon Valley`, `North Hills`, etc.
- 🏘️ **Neighborhoods** - Specific locations
  - Pittsburgh neighborhoods: `Lawrenceville`, `Shadyside`, `Oakland`, etc.
  - Allegheny municipalities: `Sewickley`, `Braddock`, `McKeesport`, etc.
- 🎯 **Confidence Scores** - Detection confidence (0-100%)
- ⏱️ **Processing Time** - Time taken per article

## 🏗️ Architecture

### Classification Pipeline

```
1. URL/Excel Input
   ↓
2. Web Scraping (BeautifulSoup)
   ↓
3. Content Extraction & Caching
   ↓
4. Advanced Geographic Classification (NLP + ML)
   - spaCy NER (Named Entity Recognition)
   - Sentence Transformers (Semantic Analysis)
   - Random Forest Classifier (Confidence Scoring)
   ↓
5. Hierarchical Assignment
   - Umbrella: Top-level location
   - Geographic Area: Mid-level region
   - Neighborhoods: Specific places
   ↓
6. Formatted Results Display
```

### Technology Stack

**Frontend:**
- Pure HTML/CSS/JavaScript (no frameworks)
- Responsive design
- Drag-and-drop file upload
- Real-time API communication

**Backend:**
- Flask API server
- pandas for data processing
- Advanced NLP pipeline:
  - spaCy for entity recognition
  - sentence-transformers for semantic analysis
  - scikit-learn for ML classification
- BeautifulSoup for web scraping

**Data Sources:**
- `enhanced_geographic_data.json` - 90 Pittsburgh neighborhoods + 127 Allegheny County municipalities
- `Pittsburgh neighborhoods.xlsx` - Detailed neighborhood data
- `Allegheny County Municipalities.xlsx` - Municipality data

## 🔍 Technical Details

### Geographic Classification Logic

**Priority Hierarchy:**
1. **Pittsburgh Neighborhoods** (highest priority)
   - 90 official city neighborhoods
   - Grouped into regions: North Side, South Pittsburgh, East End, etc.
2. **Allegheny County Municipalities** (fallback)
   - 127 boroughs and townships
   - Grouped into sub-regions: Northwest suburbs, Mon Valley, etc.

**Classification Rules:**
- If Pittsburgh neighborhoods detected → use them exclusively
- If only municipalities detected → use as neighborhoods
- Never mix Pittsburgh neighborhood regions with municipality sub-regions

### API Endpoints

#### `POST /api/test-classify`

**Single URL Request:**
```json
{
  "url": "https://www.publicsource.org/article-url/"
}
```

**Excel Upload:**
```
Content-Type: multipart/form-data
file: Excel/CSV file with "Story" column
```

**Response:**
```json
{
  "success": true,
  "results": [
    {
      "url": "...",
      "title": "Article Title",
      "author": "Author Name",
      "date": "2025-01-15T12:00:00-05:00",
      "umbrella": "Allegheny County",
      "geographic_area": "Northwest suburbs",
      "neighborhoods": "SEWICKLEY, LEET",
      "confidence_scores": {
        "SEWICKLEY": 1.0,
        "LEET": 1.0
      },
      "confidence_text": "SEWICKLEY: 100%, LEET: 100%",
      "processing_time": "2.8s"
    }
  ],
  "total_processing_time": "2.8s",
  "total_articles": 1
}
```

#### `GET /api/health`

Health check endpoint - returns server status.

## ⚠️ Important Notes

### For Local Deployment

1. **Backend must run first** on port 5001
2. **No database changes** - pure testing environment
3. **Processing time**: 2-5 seconds per article (includes web scraping)
4. **Excel format**: Must contain `Story` column with URLs

### For Vercel Deployment (Frontend Only)

**✅ What works on Vercel:**
- Static frontend hosting
- All UI interactions
- File upload interface
- Results display

**❌ What doesn't work on Vercel:**
- Backend API (serverless limitations)
- Python dependencies (spaCy, ML models)
- Large geographic database loading
- Web scraping operations

**Solution:**
```javascript
// Configure backend URL in frontend/index.html
const API_URL = 'http://YOUR-LOCAL-IP:5001/api/test-classify';
// Or use cloud hosting (AWS, GCP, Azure) for backend
```

### Why Backend Can't Deploy to Vercel

1. **Serverless timeout limits** (10s max, need 2-5s per article)
2. **Cold start issues** (ML models take time to load)
3. **Memory constraints** (NLP models require significant RAM)
4. **File size limits** (enhanced_geographic_data.json is large)
5. **External web scraping** (BeautifulSoup requests blocked)

**Recommended Backend Hosting:**
- AWS EC2 / Lambda (with layers for dependencies)
- Google Cloud Run
- Azure Functions
- Heroku
- DigitalOcean Droplet
- Self-hosted VPS

## 📁 File Structure

```
testing-tool/
├── frontend/
│   └── index.html          # Standalone frontend (Vercel-ready)
├── backend/
│   └── test_api.py         # Flask API server
├── README.md               # This file
├── QUICK_START.md          # Quick setup guide
├── LICENSE                 # MIT License
└── vercel.json             # Vercel configuration
```

## 🐛 Troubleshooting

### Cannot connect to API

**Solution:**
- Ensure backend is running: `python backend/test_api.py`
- Check port 5001 is not in use
- Check browser console for CORS errors

### Classification failed

**Solution:**
- Verify URL is accessible
- Check article can be scraped (not behind paywall)
- Check backend terminal for error logs

### Excel upload failed

**Solution:**
- Ensure file has `Story` column
- Check file format (.xlsx, .xls, .csv)
- Verify URLs start with http:// or https://

## 📞 Support

For issues or questions:
- Check [project documentation](../project-notes/IMPORTANT_NOTES_2025-01-15.md)
- Review backend terminal logs
- Test with example URL first

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

---

**Version:** 2.0
**Last Updated:** 2025-01-15
**Status:** ✅ Production Ready

**Main Project:** [PublicSource Integrated Dashboard](https://github.com/Ziyan0219/publicsource-integrated-dashboard)
