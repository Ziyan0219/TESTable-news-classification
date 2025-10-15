#!/usr/bin/env python3
"""
Quick test script to debug classification issues
"""
import sys
import os
from pathlib import Path

# Add parent to path AND change working directory to project root
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))
os.chdir(str(project_root))  # CRITICAL: Must run from project root for enhanced_geographic_data.json

from archive_classifier_final import pipeline, EnhancedGeographicDatabase
import pandas as pd

# Test URL
test_url = "https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/"

print("=" * 60)
print("CLASSIFICATION TEST")
print("=" * 60)

# Create test CSV
test_dir = Path("/tmp/quick_test")
test_dir.mkdir(parents=True, exist_ok=True)

test_csv = test_dir / "test.csv"
df = pd.DataFrame({
    'Story': [test_url],
    'Umbrella': [''],
    'GeographicArea': [''],
    'Neighborhoods': [''],
    'SocialAbstract': ['']
})
df.to_csv(test_csv, index=False)

print(f"\n1. Test CSV created: {test_csv}")

# Load geographic database
print(f"\n2. Loading geographic database...")
geo_db = EnhancedGeographicDatabase()
print(f"   - Neighborhoods: {len(geo_db.pittsburgh_neighborhoods)}")
print(f"   - Municipalities: {len(geo_db.allegheny_municipalities)}")
print(f"   - Sample: {list(geo_db.pittsburgh_neighborhoods.keys())[:3]}")

# Run pipeline
print(f"\n3. Running classification pipeline...")
neigh_path = Path(__file__).parent.parent / "Pittsburgh neighborhoods.xlsx"
muni_path = Path(__file__).parent.parent / "Allegheny County Municipalities.xlsx"
output_dir = test_dir / "output"

print(f"   - Neigh path exists: {neigh_path.exists()}")
print(f"   - Muni path exists: {muni_path.exists()}")

pipeline(test_csv, neigh_path, muni_path, output_dir, None)

# Read results
result_file = output_dir / "stories_classified_filled.csv"
if result_file.exists():
    result_df = pd.read_csv(result_file)
    print(f"\n4. RESULTS:")
    print(f"   - Umbrella: '{result_df.iloc[0]['Umbrella']}'")
    print(f"   - Geographic Area: '{result_df.iloc[0]['GeographicArea']}'")
    print(f"   - Neighborhoods: '{result_df.iloc[0]['Neighborhoods']}'")
    print(f"   - Title: '{result_df.iloc[0]['Title']}'")

    # Check if values are NaN or None
    for col in ['Umbrella', 'GeographicArea', 'Neighborhoods']:
        val = result_df.iloc[0][col]
        print(f"\n   {col}:")
        print(f"     - Value: {val}")
        print(f"     - Type: {type(val)}")
        print(f"     - Is NaN: {pd.isna(val)}")
        print(f"     - String: '{str(val)}'")
else:
    print("\n4. ERROR: Result file not found!")

print("\n" + "=" * 60)
