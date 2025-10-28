# 🚀 Complete Deployment Guide

**PublicSource Classification Testing Tool - Free Cloud Deployment**

Deploy both frontend and backend for **$0/month** using Hugging Face Spaces + Vercel.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Prerequisites](#prerequisites)
4. [Quick Start (20 Minutes)](#quick-start-20-minutes)
5. [Detailed Instructions](#detailed-instructions)
6. [Post-Deployment](#post-deployment)
7. [For End Users](#for-end-users)
8. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

### What You'll Deploy

- **Backend:** Flask API with ML classification → Hugging Face Spaces
- **Frontend:** HTML/CSS/JS testing interface → Vercel
- **Total Cost:** $0/month (free tier sufficient)

### What Users Will Get

```
User visits Vercel URL
    ↓
Enters article URL or uploads Excel
    ↓
Frontend sends request to HF backend
    ↓
Backend classifies using AI/NLP
    ↓
Results displayed instantly
```

**No installation required for end users!**

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  END USER BROWSER                                            │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Frontend (Vercel - Global CDN)                        │ │
│  │  https://your-project.vercel.app                       │ │
│  └────────────────────────────────────────────────────────┘ │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS API Calls
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  HUGGING FACE SPACES                                         │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Backend (Docker Container)                            │ │
│  │  Flask + spaCy + ML Models                            │ │
│  │  https://username-testable-news.hf.space              │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Benefits:**
- ✅ Frontend cached globally (fast load times)
- ✅ Backend has full Python + ML support
- ✅ Both auto-deploy on git push
- ✅ HTTPS by default
- ✅ No server management

---

## 📦 Prerequisites

### Accounts Needed (All Free)

1. **GitHub Account**
   - Sign up: https://github.com/signup
   - Purpose: Store and version code

2. **Hugging Face Account**
   - Sign up: https://huggingface.co/join
   - Purpose: Host backend API

3. **Vercel Account**
   - Sign up: https://vercel.com/signup
   - Use: Sign up with GitHub (easiest)
   - Purpose: Host frontend

### Files You Need

Ensure your `testing-tool` directory has:

```
testing-tool/
├── Dockerfile                              ✅ (new - created)
├── requirements.txt                        ✅ (new - created)
├── .dockerignore                          ✅ (new - created)
├── backend/
│   └── test_api.py                        ✅ (modified - standalone)
├── frontend/
│   └── index.html                         ✅ (modified - env detection)
├── archive_classifier_final.py            ✅ (copied from main project)
├── enhanced_geographic_data.json          ✅ (should exist)
├── Pittsburgh neighborhoods.xlsx          ✅ (copied)
├── Allegheny County Municipalities.xlsx   ✅ (copied)
└── HF_DEPLOYMENT_GUIDE.md                 ✅ (new - detailed guide)
```

---

## ⚡ Quick Start (20 Minutes)

### Part 1: Push to GitHub (5 minutes)

```bash
cd testing-tool

# Initialize git if needed
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for Hugging Face + Vercel deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/Ziyan0219/TESTable-news-classification.git

# Push
git branch -M main
git push -u origin main
```

---

### Part 2: Deploy Backend to Hugging Face (10 minutes)

#### 2.1 Create Space

1. Go to https://huggingface.co/new-space
2. Fill in:
   - **Space name:** `testable-news-classification`
   - **SDK:** **Docker** (IMPORTANT!)
   - **Visibility:** Public
3. Click "Create Space"

#### 2.2 Upload Files

**Option A: Web Upload (Easiest)**

1. Click "Files" tab on your Space
2. Click "Add file" → "Upload files"
3. Upload:
   ```
   Dockerfile
   requirements.txt
   .dockerignore
   backend/ (entire folder)
   archive_classifier_final.py
   enhanced_geographic_data.json
   Pittsburgh neighborhoods.xlsx
   Allegheny County Municipalities.xlsx
   ```
4. Click "Commit"

**Option B: Git Clone & Push**

```bash
# Clone your Space
git clone https://huggingface.co/spaces/YOUR-USERNAME/testable-news-classification
cd testable-news-classification

# Copy files
cp -r ../testing-tool/backend ./
cp ../testing-tool/Dockerfile ./
cp ../testing-tool/requirements.txt ./
cp ../testing-tool/.dockerignore ./
cp ../testing-tool/archive_classifier_final.py ./
cp ../testing-tool/enhanced_geographic_data.json ./
cp ../testing-tool/*.xlsx ./

# Commit and push
git add .
git commit -m "Deploy backend"
git push
```

#### 2.3 Wait for Build

- Watch "Logs" tab
- Build takes 5-15 minutes (first time only)
- Look for: `✓ Running on http://0.0.0.0:7860`

#### 2.4 Test Backend

Visit: `https://YOUR-USERNAME-testable-news-classification.hf.space/api/health`

Should see:
```json
{"status": "healthy", "service": "Classification Testing Tool"}
```

---

### Part 3: Update Frontend Config (2 minutes)

Edit `frontend/index.html` line ~457:

**Before:**
```javascript
const HF_BACKEND_URL = 'https://YOUR-USERNAME-testable-news-classification.hf.space';
```

**After (example):**
```javascript
const HF_BACKEND_URL = 'https://ziyan0219-testable-news-classification.hf.space';
```

Commit and push:
```bash
git add frontend/index.html
git commit -m "Update backend URL"
git push
```

---

### Part 4: Deploy Frontend to Vercel (3 minutes)

1. Go to https://vercel.com/new
2. Import from GitHub: `TESTable-news-classification`
3. Configure:
   - **Framework:** Other
   - **Root Directory:** `frontend`
   - **Build Command:** (leave empty)
   - **Output Directory:** `.`
4. Click "Deploy"

Wait 1-2 minutes. You'll get a URL like:
```
https://testable-news-classification.vercel.app
```

---

### Part 5: Test End-to-End (2 minutes)

1. Visit your Vercel URL
2. Should see: `✅ Connected to backend: https://...hf.space`
3. Test with URL:
   ```
   https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
   ```
4. Click "Test"
5. Wait 3-5 seconds
6. Results should appear!

---

## 📚 Detailed Instructions

For step-by-step screenshots and detailed troubleshooting, see:

- **[HF_DEPLOYMENT_GUIDE.md](HF_DEPLOYMENT_GUIDE.md)** - Complete Hugging Face setup
- **README.md** - Technical documentation
- **QUICK_START.md** - Local development setup

---

## ✅ Post-Deployment

### Monitor Your Deployments

**Hugging Face:**
- Dashboard: https://huggingface.co/spaces/YOUR-USERNAME/testable-news-classification
- Check logs regularly
- Monitor uptime and errors

**Vercel:**
- Dashboard: https://vercel.com/dashboard
- See analytics and bandwidth usage
- Monitor deployment status

### Configure Custom Domain (Optional)

**For Vercel Frontend:**
1. Go to project settings
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

**For Hugging Face Backend:**
- Not supported on free tier
- Use Hugging Face subdomain

### Set Up Monitoring (Optional)

**UptimeRobot (Free):**
1. Sign up: https://uptimerobot.com
2. Add monitor for your Vercel URL
3. Get notified if site goes down

**Better Stack (Free tier):**
1. Sign up: https://betterstack.com
2. Monitor both frontend and backend
3. Get uptime reports

### Enable Auto-Updates

**Vercel:**
- Already auto-deploys on git push to main
- Can configure preview deployments for PRs

**Hugging Face:**
- Auto-rebuilds on git push
- Can configure webhooks for GitHub integration

---

## 👥 For End Users

### How to Use (Share This)

**Simple Instructions for Non-Technical Users:**

1. **Visit the Testing Tool**
   - Go to: `https://your-project.vercel.app`
   - No installation needed, works in any browser

2. **Test Single Article**
   - Paste a PublicSource article URL
   - Example: `https://www.publicsource.org/article-url/`
   - Click "Test" button
   - Wait 3-5 seconds
   - View classification results

3. **Test Multiple Articles**
   - Prepare Excel file with "Story" column
   - Drag and drop file onto upload area
   - Wait for processing
   - View all results

4. **Copy Results**
   - Click "Copy" button
   - Paste into Word, Excel, or email

### Example URLs for Testing

```
https://www.publicsource.org/sewickley-black-history-preservation-book-film-fundraising/
https://www.publicsource.org/manchester-esplanade-development-pittsburgh-registered-community-organization-program/
https://www.publicsource.org/first-step-recovery-homes-mckeesport-addiction-center-new-facility-housing/
```

### What Results Mean

- **Umbrella:** Pittsburgh / Allegheny County / Both
- **Geographic Area:** Region grouping (North Side, Mon Valley, etc.)
- **Neighborhoods:** Specific places mentioned
- **Confidence:** How certain the AI is (0-100%)

---

## 🔧 Troubleshooting

### Issue: Backend Build Fails

**Check Dockerfile**
```bash
# Ensure Dockerfile exists in Space root
ls Dockerfile

# Verify syntax
cat Dockerfile
```

**Check Requirements**
```bash
# Ensure requirements.txt is present
ls requirements.txt

# Verify all packages are available on PyPI
```

**View Build Logs**
1. Go to your HF Space
2. Click "Logs" tab
3. Look for error messages
4. Search error on Google/HF Forums

---

### Issue: Frontend Can't Connect to Backend

**Step 1: Verify Backend URL**

Check `frontend/index.html` line ~457:
```javascript
const HF_BACKEND_URL = 'https://YOUR-USERNAME-testable-news-classification.hf.space';
```

Must match your actual HF Space URL (no trailing slash).

**Step 2: Test Backend Directly**

Visit: `https://YOUR-USERNAME-testable-news-classification.hf.space/api/health`

Should return:
```json
{"status": "healthy"}
```

If 404 or 500 error, backend has issues.

**Step 3: Check CORS**

Open browser DevTools (F12) → Console

Look for errors like:
```
CORS policy: No 'Access-Control-Allow-Origin' header
```

If found, verify `test_api.py` line ~31:
```python
CORS(app)  # This should be present
```

---

### Issue: Classification Returns Errors

**Check File Paths**

Ensure these files exist in your HF Space:
```
✅ backend/test_api.py
✅ archive_classifier_final.py
✅ enhanced_geographic_data.json
✅ Pittsburgh neighborhoods.xlsx
✅ Allegheny County Municipalities.xlsx
```

**Check Logs**

On HF Space → Logs → Look for Python errors

**Test Locally**

```bash
cd testing-tool
python backend/test_api.py

# In another terminal, test
curl -X POST http://localhost:5001/api/test-classify \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.publicsource.org/article-url/"}'
```

---

### Issue: Slow Response (10+ seconds)

**Cause: Cold Start**

Hugging Face Spaces sleep after 2-3 hours of inactivity.

**First request after sleep:**
- Takes 10-30 seconds (loading models)

**Subsequent requests:**
- Fast (2-5 seconds)

**Solutions:**

**Option 1: Accept Cold Starts (Free)**
- Inform users first request may be slow
- Show loading message

**Option 2: Keep Warm (Free, Manual)**
- Visit backend URL every hour
- Set up cron job: `curl https://your-hf-space.hf.space/api/health`

**Option 3: Upgrade to Always-On ($0.60/month)**
1. Go to HF Space settings
2. Select hardware upgrade
3. Enable "Always On"

---

### Issue: Vercel Deployment Fails

**Check Root Directory**

Should be set to: `frontend`

**Check Build Settings**
- Build Command: (empty)
- Output Directory: `.`
- Install Command: (empty)

**Check File Structure**

Vercel must see `index.html` in root of `frontend/` folder.

---

## 💰 Cost & Performance

### Free Tier (Recommended for Testing)

**Costs:**
- Hugging Face: $0/month
- Vercel: $0/month
- **Total: $0/month**

**Performance:**
- Frontend load: < 1 second (global CDN)
- Backend response: 2-5 seconds (warm)
- Backend cold start: 10-30 seconds (after sleep)
- Monthly requests: Unlimited (reasonable use)

**Limitations:**
- Backend sleeps after 2-3 hours inactive
- 2 CPU cores, 16GB RAM
- Community support only

### Upgraded Tier (Optional)

**Costs:**
- HF CPU Basic: $0.60/month (always-on)
- HF CPU Medium: $3/month (4 vCPU, 32GB RAM)
- Vercel Pro: $20/month (team features, analytics)

**Benefits:**
- No cold starts
- More resources
- Priority support
- Custom domains (both)
- Advanced analytics

---

## 📊 Deployment Checklist

Before announcing to users:

### Pre-Deployment
- [ ] All files in GitHub repository
- [ ] Dockerfile syntax verified
- [ ] requirements.txt complete
- [ ] Dependencies tested locally
- [ ] Frontend config updated with HF URL

### Deployment
- [ ] HF Space created with Docker SDK
- [ ] All files uploaded to HF Space
- [ ] Build completed successfully (check logs)
- [ ] Health endpoint returns 200 OK
- [ ] Vercel project imported from GitHub
- [ ] Vercel deployment successful
- [ ] Custom domain configured (if applicable)

### Testing
- [ ] Frontend loads without errors
- [ ] Backend connection successful
- [ ] Single URL test works end-to-end
- [ ] Excel batch upload works
- [ ] Results display correctly
- [ ] All classification fields populated
- [ ] Copy button works
- [ ] Clear button works
- [ ] Mobile responsive (test on phone)
- [ ] Browser console has no errors

### Documentation
- [ ] README updated with deployment URLs
- [ ] User guide prepared
- [ ] Example test URLs documented
- [ ] Troubleshooting guide accessible
- [ ] Support contact info provided

---

## 🎉 Success!

You now have a fully deployed, production-ready classification testing tool!

### Share These URLs

**For Testing:**
```
Frontend: https://your-project.vercel.app
Backend API: https://your-username-testable-news.hf.space
Health Check: https://your-username-testable-news.hf.space/api/health
```

### Key Features

✅ **Completely Free** ($0/month)
✅ **No Installation** (users just visit URL)
✅ **Global CDN** (fast worldwide)
✅ **Auto-deploys** (git push → live in minutes)
✅ **HTTPS Secure** (SSL certificates included)
✅ **Scalable** (handles reasonable traffic)
✅ **Mobile Friendly** (responsive design)

### Next Steps

1. **Share with Team**
   - Send Vercel URL
   - Provide usage instructions
   - Collect feedback

2. **Monitor Performance**
   - Check HF Space logs weekly
   - Monitor Vercel analytics
   - Track error rates

3. **Iterate**
   - Fix bugs as reported
   - Add features if needed
   - Optimize performance

4. **Scale If Needed**
   - Upgrade HF hardware if slow
   - Add custom domain
   - Set up monitoring alerts

---

## 📞 Support Resources

### Documentation
- **This Guide:** Complete deployment instructions
- **[HF_DEPLOYMENT_GUIDE.md](HF_DEPLOYMENT_GUIDE.md):** Hugging Face detailed steps
- **[README.md](README.md):** Technical documentation
- **[QUICK_START.md](QUICK_START.md):** Local development

### Community
- **Hugging Face Forum:** https://discuss.huggingface.co/
- **Vercel Discord:** https://vercel.com/discord
- **GitHub Issues:** https://github.com/Ziyan0219/TESTable-news-classification/issues

### Helpful Links
- **HF Spaces Docs:** https://huggingface.co/docs/hub/spaces
- **Vercel Docs:** https://vercel.com/docs
- **Docker Docs:** https://docs.docker.com/

---

**🚀 Happy Deploying!**

**Version:** 1.0
**Last Updated:** 2025-01-15
**Status:** Production Ready

**Made with ❤️ for PublicSource news classification**
