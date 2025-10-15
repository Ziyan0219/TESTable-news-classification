# Quick Start Guide

## Start Testing in 5 Minutes

### Step 1: Start the Backend API

Open Command Prompt or PowerShell and run:

```bash
cd C:\Users\32044\Desktop\agents\publicsource-integrated-dashboard\testing-tool\backend
python test_api.py
```

**Success Indicator** ✅:
```
============================================================
PublicSource Classification Testing Tool
============================================================
Starting server on http://localhost:5001
...
```

⚠️ **Keep this window open! Do not close it!**

---

### Step 2: Open the Testing Page

**Method A (Recommended)**: Double-click the file
1. Open File Explorer
2. Navigate to: `C:\Users\32044\Desktop\agents\publicsource-integrated-dashboard\testing-tool\frontend\`
3. Double-click `index.html`
4. Your browser will open the testing page

**Method B**: Use HTTP server
```bash
cd C:\Users\32044\Desktop\agents\publicsource-integrated-dashboard\testing-tool\frontend
python -m http.server 8080
```
Then visit: http://localhost:8080

---

### Step 3: Start Testing!

#### Test a Single URL:
1. Copy a PublicSource article URL, for example:
   ```
   https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
   ```
2. Paste it into the "Single URL Test" input box
3. Click "Test" button
4. Wait 2-5 seconds and view the classification results!

#### Test Excel File:
1. Prepare an Excel file with a `Story` column
2. Drag and drop it to the "Excel Batch Test" area
3. Wait for processing
4. View all classification results

---

## Example Test URLs

Use these URLs for testing:

```
https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
https://www.publicsource.org/manchester-esplanade-development-pittsburgh-registered-community-organization-program/
https://www.publicsource.org/first-step-recovery-homes-mckeesport-addiction-center-new-facility-housing/
```

---

## FAQ

### Q: Page shows "Cannot connect to API server"?
**A:** Ensure Step 1 backend service is running. Check http://localhost:5001/api/health

### Q: How long does classification take?
**A:** ~2-5 seconds per article (includes web scraping and AI analysis)

### Q: Are test results saved?
**A:** No! This is a pure testing environment that doesn't affect the main database

### Q: Excel file format?
**A:** Must contain a `Story` column with one URL per row. Supports .xlsx, .xls, .csv

---

## Results Explanation

Classification results include:
- **Umbrella**: Pittsburgh / Allegheny County / Pittsburgh, Allegheny County
- **Geographic Area**: North Side, South Side, Central Pittsburgh, etc.
- **Neighborhoods**: Specific neighborhood names
- **Confidence**: Confidence scores (0-100%)
- **Title, Author, Date**: Article metadata

---

## Tips

1. ✅ Copy all results (click "Copy" button)
2. ✅ Drag and drop Excel files supported
3. ✅ Classification logic identical to main dashboard
4. ✅ Designed for non-technical users

---

**Need Help?** See full documentation: `testing-tool/README.md`
