# 📖 Complete User Guide: PublicSource Classification Testing Tool

**From Zero to Testing in 15 Minutes**

This guide will walk you through everything from getting the code to testing article classifications. No technical background required!

---

## 📑 Table of Contents

1. [What Is This Tool?](#what-is-this-tool)
2. [Prerequisites](#prerequisites)
3. [Getting the Code](#getting-the-code)
4. [Setting Up Your Environment](#setting-up-your-environment)
5. [Starting the Testing Panel](#starting-the-testing-panel)
6. [Using the Testing Tool](#using-the-testing-tool)
7. [Understanding Results](#understanding-results)
8. [Troubleshooting](#troubleshooting)
9. [Project Structure](#project-structure)
10. [FAQ](#faq)

---

## 🎯 What Is This Tool?

The **PublicSource Classification Testing Tool** is a standalone application that helps you test how well our system classifies news articles by geographic location.

**What it does:**
- Takes a PublicSource article URL
- Automatically extracts the article content
- Uses AI to identify which Pittsburgh neighborhoods or Allegheny County municipalities are mentioned
- Shows you the classification results instantly

**Important:** This is a testing-only tool. Results are NOT saved to any database.

---

## 📦 Prerequisites

Before you start, you'll need to install these programs on your computer:

### 1. Git (Version Control)

**What it is:** A tool that helps you download code from GitHub.

**Download & Install:**
- Visit: https://git-scm.com/downloads
- Download for your operating system (Windows/Mac/Linux)
- Run the installer
- Use default settings (just keep clicking "Next")

**Verify Installation:**
```bash
git --version
```
You should see something like: `git version 2.40.0`

---

### 2. Python 3.11 or Higher

**What it is:** The programming language our backend uses.

**Download & Install:**
- Visit: https://www.python.org/downloads/
- Download Python 3.11 or newer
- **IMPORTANT:** During installation, check the box that says "Add Python to PATH"
- Complete the installation

**Verify Installation:**
```bash
python --version
```
You should see: `Python 3.11.x` or higher

**If `python` doesn't work, try:**
```bash
python3 --version
```

---

### 3. Web Browser

Any modern browser works:
- Chrome (recommended)
- Firefox
- Edge
- Safari

---

## 🚀 Getting the Code

Now let's download the project from GitHub!

### Step 1: Choose a Location

Decide where you want to store the project. For example:
- Windows: `C:\Users\YourName\Projects\`
- Mac/Linux: `~/Projects/`

### Step 2: Open Terminal/Command Prompt

**Windows:**
- Press `Windows Key + R`
- Type: `cmd`
- Press Enter

**Mac:**
- Press `Command + Space`
- Type: `terminal`
- Press Enter

**Linux:**
- Press `Ctrl + Alt + T`

### Step 3: Navigate to Your Chosen Location

```bash
# Windows example
cd C:\Users\YourName\Projects

# Mac/Linux example
cd ~/Projects
```

### Step 4: Clone the Repository

Copy and paste this command:

```bash
git clone https://github.com/Ziyan0219/publicsource-integrated-dashboard.git
```

**What you'll see:**
```
Cloning into 'publicsource-integrated-dashboard'...
remote: Enumerating objects: 1234, done.
remote: Counting objects: 100% (1234/1234), done.
remote: Compressing objects: 100% (789/789), done.
remote: Total 1234 (delta 445), reused 1234 (delta 445)
Receiving objects: 100% (1234/1234), 5.67 MiB | 3.45 MiB/s, done.
Resolving deltas: 100% (445/445), done.
```

### Step 5: Navigate to Testing Tool Directory

```bash
cd publicsource-integrated-dashboard/testing-tool
```

### Step 6: Verify You're in the Right Place

```bash
# Windows
dir

# Mac/Linux
ls
```

You should see these folders and files:
- `backend/`
- `frontend/`
- `README.md`
- `QUICK_START.md`
- `COMPLETE_USER_GUIDE.md` (this file!)

✅ **Success!** You now have the code on your computer.

---

## ⚙️ Setting Up Your Environment

Now we need to install the required Python libraries.

### Step 1: Navigate to Parent Directory

First, go back to the main project folder:

```bash
cd ..
```

You should now be in: `publicsource-integrated-dashboard/`

### Step 2: Install Python Dependencies

Run this command:

```bash
pip install -r requirements.txt
```

**If `pip` doesn't work, try:**
```bash
pip3 install -r requirements.txt
```

**Or on Mac/Linux:**
```bash
python3 -m pip install -r requirements.txt
```

**What you'll see:**
```
Collecting flask==3.1.0
Downloading Flask-3.1.0-py3-none-any.whl
Collecting pandas==2.2.3
...
Successfully installed flask-3.1.0 pandas-2.2.3 ...
```

⏳ **This will take 3-5 minutes.** The system is downloading and installing about 20-30 libraries.

### Step 3: Download spaCy Language Model

spaCy is the AI library that helps identify place names. Run:

```bash
python -m spacy download en_core_web_sm
```

**Or:**
```bash
python3 -m spacy download en_core_web_sm
```

**What you'll see:**
```
Collecting en-core-web-sm==3.7.1
✔ Download and installation successful
```

### Step 4: Verify Installation

Test that everything is installed:

```bash
python -c "import flask, pandas, spacy; print('✅ All dependencies installed successfully!')"
```

If you see `✅ All dependencies installed successfully!`, you're ready to proceed!

---

## 🚦 Starting the Testing Panel

Now the fun part - let's start the testing tool!

### Part A: Start the Backend Server

**What this does:** The backend server processes article URLs and performs the AI classification.

#### Step 1: Open Terminal and Navigate to Backend

```bash
cd testing-tool/backend
```

**Full path from project root:**
```bash
# From publicsource-integrated-dashboard/
cd testing-tool/backend
```

#### Step 2: Start the Server

```bash
python test_api.py
```

**Or:**
```bash
python3 test_api.py
```

#### Step 3: Wait for Success Message

You should see:

```
============================================================
PublicSource Classification Testing Tool
============================================================
Loading enhanced geographic data...
✓ Loaded 90 Pittsburgh neighborhoods
✓ Loaded 127 Allegheny County municipalities
✓ Total geographic entities: 217

Initializing classification system...
✓ Classification system ready

Starting server on http://localhost:5001
Press CTRL+C to quit

* Serving Flask app 'test_api'
* Debug mode: on
WARNING: This is a development server. Do not use it in production.
* Running on http://127.0.0.1:5001
```

✅ **Server is running!**

⚠️ **IMPORTANT:** Keep this terminal window open! Do NOT close it. The backend must keep running while you use the testing tool.

---

### Part B: Open the Frontend

Now we'll open the user interface.

#### Method 1: Direct File Open (Easiest)

1. Open File Explorer (Windows) or Finder (Mac)
2. Navigate to: `publicsource-integrated-dashboard/testing-tool/frontend/`
3. Find the file: `index.html`
4. **Double-click** it

Your default browser will open with the testing interface!

#### Method 2: Using HTTP Server

Open a **NEW** terminal window (keep the backend running in the first one):

```bash
# Navigate to frontend directory
cd publicsource-integrated-dashboard/testing-tool/frontend

# Start a simple HTTP server
python -m http.server 8080
```

Then open your browser and visit: **http://localhost:8080**

---

### Part C: Verify Connection

On the web page, you should see:

```
PublicSource Classification Testing Tool
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔌 Status: Connected to API server
```

✅ **You're ready to test!**

If you see "Cannot connect to API server" instead, see [Troubleshooting](#troubleshooting).

---

## 🧪 Using the Testing Tool

Now let's test some article classifications!

### Test Method 1: Single URL Test

**Best for:** Quick testing of one article at a time.

#### Step 1: Get an Article URL

Copy a PublicSource article URL. For example:
```
https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
```

**More test URLs:**
```
https://www.publicsource.org/manchester-esplanade-development-pittsburgh-registered-community-organization-program/
https://www.publicsource.org/first-step-recovery-homes-mckeesport-addiction-center-new-facility-housing/
```

#### Step 2: Paste the URL

1. Find the **"Single URL Test"** section on the page
2. Look for the input box labeled "Article URL"
3. Click inside the box
4. Paste your URL (Ctrl+V or Command+V)

#### Step 3: Click "Test"

Click the blue **"🧪 Test"** button.

#### Step 4: Wait for Results

You'll see:
```
⏳ Classifying article... (this may take a few seconds)
```

⏱️ **Processing time:** 2-5 seconds per article

#### Step 5: View Results

After processing completes, you'll see detailed results like:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Classification Result #1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 URL: https://www.publicsource.org/sewickley-...
📰 Title: Sewickley community preserves Black history through book and film
✍️ Author: Ashley Murray
📅 Date: 2024-10-15T09:30:00-04:00

📊 CLASSIFICATION:
  🏠 Umbrella:        Allegheny County
  📍 Geographic Area: Northwest suburbs
  🏘️ Neighborhoods:   SEWICKLEY, LEET

🎯 CONFIDENCE SCORES:
  SEWICKLEY: 100%
  LEET: 100%

⏱️ Processing time: 2.8s
```

---

### Test Method 2: Excel Batch Test

**Best for:** Testing multiple articles at once.

#### Step 1: Prepare Your Excel File

Create an Excel file (.xlsx, .xls, or .csv) with this structure:

| Story |
|-------|
| https://www.publicsource.org/article-1/ |
| https://www.publicsource.org/article-2/ |
| https://www.publicsource.org/article-3/ |

**Requirements:**
- ✅ Must have a column named **"Story"** (exact spelling)
- ✅ Each row contains one URL
- ✅ URLs should start with `http://` or `https://`
- ✅ Supported formats: `.xlsx`, `.xls`, `.csv`

**Example file is provided:** `testing-tool/example_test.xlsx`

#### Step 2: Upload the File

**Option A: Drag and Drop**
1. Find the **"Excel Batch Test"** section
2. Drag your Excel file from File Explorer/Finder
3. Drop it onto the dashed box area

**Option B: Click to Select**
1. Click anywhere inside the dashed box
2. A file selection dialog will appear
3. Navigate to your Excel file
4. Select it and click "Open"

#### Step 3: Wait for Processing

The system will:
1. Read all URLs from your Excel file
2. Process each article one by one
3. Display a progress indicator

```
⏳ Processing article 1 of 5...
⏳ Processing article 2 of 5...
⏳ Processing article 3 of 5...
```

#### Step 4: View All Results

After processing completes, you'll see results for each article in order.

---

### Additional Features

#### Copy All Results

Click the **"📋 Copy"** button at the top of the results section.

All results will be copied to your clipboard. You can then:
- Paste into Word (Ctrl+V / Command+V)
- Paste into Excel
- Paste into an email
- Save for documentation

#### Clear Results

Click the **"🗑️ Clear"** button to remove all displayed results and start fresh.

---

## 📊 Understanding Results

Let's break down what each field means:

### Basic Information

| Field | Meaning | Example |
|-------|---------|---------|
| **URL** | The article's web address | `https://www.publicsource.org/...` |
| **Title** | Article headline | "Sewickley community preserves Black history" |
| **Author** | Who wrote the article | "Ashley Murray" |
| **Date** | Publication date | "2024-10-15" |

### Classification Fields

#### 🏠 Umbrella (Top-Level Category)

This indicates the broadest geographic scope:

- **"Pittsburgh"** - Article focuses on Pittsburgh city neighborhoods
- **"Allegheny County"** - Article focuses on municipalities outside Pittsburgh
- **"Pittsburgh, Allegheny County"** - Article covers both
- **"General Interest"** - No specific geographic focus detected

#### 📍 Geographic Area (Regional Grouping)

**For Pittsburgh neighborhoods:**
- North Side
- South Pittsburgh
- East End
- Central Pittsburgh
- West End

**For Allegheny County municipalities:**
- Northwest suburbs (e.g., Sewickley, Bellevue)
- Mon Valley (e.g., Braddock, McKeesport)
- North Hills (e.g., Ross, Shaler)
- South Hills (e.g., Bethel Park, Mt. Lebanon)
- Eastern suburbs (e.g., Penn Hills, Wilkinsburg)

#### 🏘️ Neighborhoods (Specific Locations)

**Pittsburgh Neighborhoods (90 total):**
Examples: Lawrenceville, Shadyside, Oakland, Squirrel Hill, Bloomfield, Strip District, Downtown, Highland Park, etc.

**Allegheny County Municipalities (127 total):**
Examples: Sewickley, Braddock, McKeesport, Wilkinsburg, Homestead, Moon Township, etc.

#### 🎯 Confidence Scores

Shows how confident the AI is about each location detection:

- **90-100%** - Very confident (location clearly mentioned with context)
- **70-89%** - Confident (location mentioned with some context)
- **50-69%** - Moderate confidence (location mentioned but limited context)
- **Below 50%** - Low confidence (usually filtered out)

**Example:**
```
SEWICKLEY: 100%
LEET: 95%
```
This means the AI is certain about Sewickley and very confident about Leet.

#### ⏱️ Processing Time

How long it took to:
1. Fetch the article from the web
2. Extract the text content
3. Analyze with AI
4. Generate classification results

**Typical times:** 2-5 seconds per article

---

## 🔧 Troubleshooting

### Problem: "Cannot connect to API server"

**Symptoms:**
- Red error message on frontend
- Tests don't work
- No results appear

**Solutions:**

1. **Check if backend is running**
   - Look at the terminal where you ran `python test_api.py`
   - Is it still open and showing logs?
   - If closed, restart it (see [Starting the Testing Panel](#starting-the-testing-panel))

2. **Verify backend URL**
   - Backend should be at: `http://localhost:5001`
   - Test in browser: Open `http://localhost:5001/api/health`
   - Should see: `{"status": "healthy"}`

3. **Check firewall**
   - Your firewall might be blocking port 5001
   - Temporarily disable firewall or allow Python

4. **Check port availability**
   ```bash
   # Windows
   netstat -an | findstr "5001"

   # Mac/Linux
   lsof -i :5001
   ```

   If another program is using port 5001, stop it or change the backend port.

---

### Problem: "Module not found" Error

**Symptoms:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**

Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

Or install specific missing module:
```bash
pip install flask
pip install pandas
pip install beautifulsoup4
```

---

### Problem: Excel Upload Fails

**Symptoms:**
- File uploads but no results
- Error message about missing "Story" column

**Solutions:**

1. **Check column name**
   - Column must be named exactly **"Story"** (capital S)
   - No extra spaces
   - Not "story", "STORY", or "Stories"

2. **Check file format**
   - Must be .xlsx, .xls, or .csv
   - Other formats won't work

3. **Check URLs**
   - Each cell should contain a full URL
   - Must start with `http://` or `https://`
   - One URL per cell

4. **Try example file**
   - Use `testing-tool/example_test.xlsx`
   - If this works, compare with your file

---

### Problem: Classification Results Look Wrong

**Symptoms:**
- Places detected that aren't in the article
- Expected places missing
- Confidence scores seem off

**This is normal because:**
- The AI isn't perfect
- This is exactly why we have a testing tool!
- Use these results to evaluate and improve the classification logic

**What to do:**
1. Copy the results
2. Note which classifications were wrong
3. Share with the development team
4. This feedback helps improve the system

---

### Problem: Very Slow Processing

**Symptoms:**
- Each article takes 10+ seconds
- System seems frozen

**Solutions:**

1. **Check internet connection**
   - System needs to fetch articles from publicsource.org
   - Slow connection = slow processing

2. **Check article accessibility**
   - Can you open the URL in a browser?
   - Is the website responding?

3. **Restart backend**
   - Close the backend terminal (Ctrl+C)
   - Restart: `python test_api.py`

---

### Problem: Python Command Not Found

**Symptoms:**
```bash
'python' is not recognized as an internal or external command
```

**Solutions:**

1. **Try `python3` instead:**
   ```bash
   python3 test_api.py
   python3 -m pip install -r requirements.txt
   ```

2. **Reinstall Python**
   - Download from python.org
   - **Check "Add Python to PATH" during installation**

3. **Manually add to PATH**
   - Windows: Search "Environment Variables" → Edit PATH → Add Python folder
   - Mac/Linux: Add to `~/.bashrc` or `~/.zshrc`

---

## 📁 Project Structure

Understanding the project layout:

```
publicsource-integrated-dashboard/
│
├── frontend/                          # Main dashboard (React application)
├── src/                              # Main dashboard backend (Flask)
├── testing-tool/                     # ← TESTING TOOL (what this guide is about)
│   │
│   ├── frontend/
│   │   └── index.html               # Testing interface (open this in browser)
│   │
│   ├── backend/
│   │   └── test_api.py             # Testing API server (run this)
│   │
│   ├── COMPLETE_USER_GUIDE.md      # ← YOU ARE HERE
│   ├── README.md                    # Technical documentation
│   ├── QUICK_START.md               # Quick setup guide (5 minutes)
│   ├── DEPLOYMENT.md                # Cloud deployment instructions
│   ├── GITHUB_SETUP.md              # GitHub repository setup
│   └── example_test.xlsx            # Sample Excel file for testing
│
├── archive_classifier_final.py       # Main classification logic
├── advanced_geographic_classifier.py # Advanced NLP classifier
├── enhanced_geographic_data.json    # Geographic database (90 neighborhoods + 127 municipalities)
├── Pittsburgh neighborhoods.xlsx     # Pittsburgh neighborhood reference data
├── Allegheny County Municipalities.xlsx  # Allegheny County reference data
├── requirements.txt                 # Python dependencies
└── CLAUDE.md                        # Development guidelines
```

### Key Differences: Main Dashboard vs Testing Tool

| Feature | Main Dashboard | Testing Tool |
|---------|----------------|--------------|
| **Purpose** | Production data management | Testing classification accuracy |
| **Database** | Saves to stories.json | No database (results not saved) |
| **Users** | End users managing articles | Developers/testers evaluating accuracy |
| **Tech Stack** | React + Flask + SQLite | Pure HTML/CSS/JS + Flask |
| **Deployment** | Production server | Can run locally or cloud |

---

## ❓ FAQ

### General Questions

**Q: Do test results get saved anywhere?**
A: No. This is a pure testing environment. Results are displayed only and not saved to any database.

**Q: Can I use this for articles from other news sites?**
A: The classification logic will work, but it's optimized for PublicSource articles about Pittsburgh/Allegheny County.

**Q: How accurate is the classification?**
A: Typically 90-95% accurate for clear geographic references. Ambiguous cases may have lower accuracy.

**Q: Can I test more than 100 articles at once?**
A: Yes, but processing time increases (2-5 seconds per article). 100 articles = 3-8 minutes.

---

### Technical Questions

**Q: What AI/ML models are used?**
A:
- **spaCy** for named entity recognition
- **sentence-transformers** for semantic analysis
- **Random Forest** for confidence scoring
- Custom rule-based geographic validation

**Q: Where is the geographic database stored?**
A: `enhanced_geographic_data.json` contains 217 locations (90 Pittsburgh neighborhoods + 127 Allegheny County municipalities).

**Q: Can I modify the classification logic?**
A: Yes! See `backend/test_api.py` and the main project's `archive_classifier_final.py`.

**Q: Does this require an API key?**
A: No. All classification runs locally. No external API calls (except fetching articles).

---

### Deployment Questions

**Q: Can I deploy this online?**
A: Yes! See `DEPLOYMENT.md` for instructions on deploying to:
- Vercel (frontend only - FREE)
- AWS EC2 (backend - ~$5/month)
- Google Cloud Run
- Heroku

**Q: Can multiple people use it at once?**
A: Yes, if deployed to a cloud server. Local setup is single-user.

**Q: What about the online demo?**
A: Visit: https://testable-news-classification.vercel.app
(Note: You'll need to self-host the backend)

---

## 🎉 Success Checklist

You've successfully set up the testing tool when:

- ✅ Git clone completed without errors
- ✅ Python dependencies installed (including spaCy model)
- ✅ Backend server starts and shows "Running on http://127.0.0.1:5001"
- ✅ Frontend opens in browser
- ✅ Status shows "Connected to API server"
- ✅ Test URL returns classification results within 5 seconds
- ✅ Excel upload processes all articles successfully
- ✅ Results display correctly with all fields
- ✅ Copy button works
- ✅ Clear button works

---

## 📞 Getting Help

### Documentation Resources

- **This Guide:** Complete setup and usage instructions
- **QUICK_START.md:** Fast 5-minute setup (experienced users)
- **README.md:** Technical documentation and API reference
- **DEPLOYMENT.md:** Cloud deployment instructions
- **GITHUB_SETUP.md:** GitHub repository management

### Support Channels

1. **Check existing documentation** (usually answers 90% of questions)
2. **Review troubleshooting section** in this guide
3. **Check terminal/console** for error messages
4. **Test with example files** to isolate the issue
5. **Create GitHub issue** with details:
   - What you were trying to do
   - What happened instead
   - Error messages (full text)
   - Your OS and Python version

### GitHub Repository

Main Project: https://github.com/Ziyan0219/publicsource-integrated-dashboard

---

## 🚀 Next Steps

Now that you have the testing tool running:

### For Testing
1. Test with various PublicSource articles
2. Compare results with actual article content
3. Note any misclassifications
4. Test edge cases (articles mentioning multiple locations)

### For Development
1. Review classification logic in `backend/test_api.py`
2. Explore the main project's classification pipeline
3. Understand the geographic database structure
4. Consider improvements to classification rules

### For Deployment
1. If satisfied with local testing, consider cloud deployment
2. See `DEPLOYMENT.md` for Vercel + AWS setup
3. Share with team members for collaborative testing

---

## 📄 License

This project is licensed under the MIT License.

You are free to:
- Use commercially
- Modify
- Distribute
- Sublicense

See the `LICENSE` file for full details.

---

## 🙏 Acknowledgments

**Main Project:** PublicSource Integrated Dashboard
**GitHub:** https://github.com/Ziyan0219/publicsource-integrated-dashboard
**Classification Logic:** Advanced NLP with spaCy, sentence-transformers, and scikit-learn
**Geographic Data:** Pittsburgh neighborhoods and Allegheny County municipalities

---

## 📊 Quick Reference Card

**Backend Start:**
```bash
cd testing-tool/backend
python test_api.py
```

**Frontend Open:**
```bash
# Method 1: Double-click frontend/index.html

# Method 2:
cd testing-tool/frontend
python -m http.server 8080
# Open http://localhost:8080
```

**Test URL Examples:**
```
https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
https://www.publicsource.org/manchester-esplanade-development-pittsburgh-registered-community-organization-program/
```

**Important URLs:**
- Backend API: http://localhost:5001
- Health Check: http://localhost:5001/api/health
- Frontend: Open `frontend/index.html` in browser

**Common Commands:**
```bash
# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Check Python version
python --version

# Check Git version
git --version
```

---

**Version:** 2.0
**Last Updated:** 2025-01-15
**Status:** ✅ Production Ready

**Happy Testing! 🎯**

---

*For the latest version of this guide, visit: https://github.com/Ziyan0219/publicsource-integrated-dashboard/tree/main/testing-tool*
