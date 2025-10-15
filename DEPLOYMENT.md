# Deployment Guide

## Vercel Deployment (Frontend Only)

### ✅ What You Can Deploy to Vercel

- **Frontend** (`frontend/index.html`)
  - Static HTML/CSS/JavaScript
  - All UI components
  - File upload interface
  - Results display formatting

### ❌ What You Cannot Deploy to Vercel

- **Backend API** (`backend/test_api.py`)
  - Requires Python runtime
  - Uses heavy ML libraries (spaCy, transformers)
  - Needs web scraping (BeautifulSoup)
  - Processing time exceeds serverless limits (2-5s per article)

---

## Frontend Deployment to Vercel

### Step 1: Prepare Repository

```bash
cd testing-tool
git init
git add .
git commit -m "Initial commit"
```

### Step 2: Deploy to Vercel

#### Option A: Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Follow prompts:
# - Link to existing project or create new
# - Confirm settings
# - Deploy
```

#### Option B: Using Vercel Dashboard

1. Visit [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import from Git repository: `TESTable-news-classification`
4. Configure:
   - Framework Preset: Other
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: `frontend`
5. Click "Deploy"

### Step 3: Configure Backend URL

After deployment, update the API URL in `frontend/index.html`:

```javascript
// Line 449
const API_URL = 'http://YOUR-BACKEND-URL:5001/api/test-classify';
```

Replace `YOUR-BACKEND-URL` with:
- `localhost` for local testing
- Your server IP for remote backend
- Your cloud hosting URL (AWS, GCP, etc.)

---

## Backend Deployment Options

### Option 1: AWS EC2 (Recommended)

**Pros:**
- Full control over environment
- No serverless limitations
- Can run ML models
- Persistent server

**Steps:**
1. Launch EC2 instance (Ubuntu 20.04+)
2. Install Python 3.11+
3. Clone repository
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
5. Run with PM2 for persistence:
   ```bash
   pm2 start backend/test_api.py --interpreter python3
   ```
6. Configure security group to allow port 5001

**Cost:** ~$5-10/month for t2.micro

### Option 2: Google Cloud Run

**Pros:**
- Serverless but with longer timeouts (60s)
- Auto-scaling
- Pay per use

**Steps:**
1. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY backend/ /app/backend/
   COPY requirements.txt /app/
   RUN pip install -r requirements.txt
   RUN python -m spacy download en_core_web_sm
   EXPOSE 5001
   CMD ["python", "backend/test_api.py"]
   ```
2. Deploy:
   ```bash
   gcloud run deploy testable-api \
     --source . \
     --region us-central1 \
     --allow-unauthenticated \
     --timeout 60s \
     --memory 2Gi
   ```

**Cost:** ~$0-5/month (free tier available)

### Option 3: Heroku

**Pros:**
- Easy deployment
- Free tier available
- Automatic SSL

**Steps:**
1. Create `Procfile`:
   ```
   web: python backend/test_api.py
   ```
2. Create `runtime.txt`:
   ```
   python-3.11.0
   ```
3. Deploy:
   ```bash
   heroku create testable-classification-api
   heroku buildpacks:add --index 1 heroku/python
   git push heroku main
   ```

**Cost:** Free tier available (with sleep), $7/month for hobby tier

### Option 4: DigitalOcean Droplet

**Pros:**
- Simple VPS
- Predictable pricing
- Full control

**Steps:**
1. Create droplet (Ubuntu 20.04)
2. SSH and setup:
   ```bash
   apt update && apt install python3.11 python3-pip
   git clone https://github.com/Ziyan0219/TESTable-news-classification.git
   cd TESTable-news-classification/testing-tool
   pip install -r ../../requirements.txt
   python -m spacy download en_core_web_sm
   ```
3. Run with systemd service or PM2

**Cost:** $6/month for basic droplet

### Option 5: Azure Functions (Advanced)

**Pros:**
- Serverless on Azure
- Good Python support
- Longer timeouts available

**Steps:**
1. Install Azure Functions Core Tools
2. Create function app
3. Configure with Premium plan (for longer timeouts)
4. Deploy

**Cost:** ~$10-20/month for Premium plan

---

## Recommended Architecture

```
┌─────────────────┐
│                 │
│  Vercel (Free)  │  ← Frontend hosting
│                 │
└────────┬────────┘
         │ API calls
         ↓
┌─────────────────┐
│                 │
│  AWS EC2 / GCP  │  ← Backend hosting
│  Cloud Run      │
│                 │
└─────────────────┘
```

**Why this works:**
- Frontend on Vercel: Fast CDN, free SSL, auto-deploy
- Backend on cloud: Persistent, handles ML models, no timeout issues
- CORS enabled for cross-origin requests

---

## Environment Configuration

### Backend Environment Variables

Create `.env` file:
```bash
# Optional: OpenAI API key for teaser generation (currently disabled)
OPENAI_API_KEY=your_key_here

# Flask configuration
FLASK_ENV=production
PORT=5001

# CORS origins (comma-separated)
CORS_ORIGINS=https://testable-news-classification.vercel.app,http://localhost:8080
```

### Frontend Configuration

Update in `frontend/index.html`:
```javascript
// Production API URL
const API_URL = 'https://your-backend.example.com/api/test-classify';

// Or use environment detection
const API_URL = window.location.hostname === 'localhost'
  ? 'http://localhost:5001/api/test-classify'
  : 'https://your-backend.example.com/api/test-classify';
```

---

## Security Considerations

### Backend Security

1. **Enable rate limiting:**
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app, default_limits=["100 per hour"])
   ```

2. **Add authentication (optional):**
   ```python
   @app.before_request
   def verify_token():
       token = request.headers.get('Authorization')
       if token != os.environ.get('API_TOKEN'):
           return jsonify({'error': 'Unauthorized'}), 401
   ```

3. **Use HTTPS** (automatic with Vercel, configure on backend)

### Frontend Security

1. **Content Security Policy:**
   ```html
   <meta http-equiv="Content-Security-Policy"
         content="default-src 'self'; script-src 'self' 'unsafe-inline'; connect-src *">
   ```

2. **Input validation** (already implemented)

---

## Monitoring & Logs

### Backend Monitoring

1. **Add logging:**
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   app.logger.info('Classification request received')
   ```

2. **Use monitoring services:**
   - Sentry for error tracking
   - New Relic for performance
   - CloudWatch/Stackdriver for cloud deployments

### Frontend Monitoring

1. **Google Analytics:**
   ```html
   <!-- Add to frontend/index.html -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
   ```

2. **Error tracking:**
   ```javascript
   window.addEventListener('error', (e) => {
       // Send to error tracking service
       console.error('Frontend error:', e);
   });
   ```

---

## Performance Optimization

### Backend

1. **Cache article content** (already implemented)
2. **Use connection pooling** for database/API calls
3. **Enable gzip compression:**
   ```python
   from flask_compress import Compress
   Compress(app)
   ```

### Frontend

1. **Minify HTML/CSS/JS** (Vercel does automatically)
2. **Use CDN** (Vercel provides)
3. **Lazy load non-critical resources**

---

## Testing Deployment

### Test Checklist

- [ ] Frontend loads correctly
- [ ] API health endpoint responds
- [ ] Single URL classification works
- [ ] Excel upload works
- [ ] Results display properly
- [ ] Copy/Clear buttons work
- [ ] Error messages show correctly
- [ ] CORS is properly configured
- [ ] SSL/HTTPS works
- [ ] Mobile responsiveness

### Test Commands

```bash
# Test backend health
curl https://your-backend.example.com/api/health

# Test classification
curl -X POST https://your-backend.example.com/api/test-classify \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.publicsource.org/test-article/"}'
```

---

## Rollback Plan

If deployment fails:

1. **Frontend:** Vercel keeps previous deployments, can rollback in dashboard
2. **Backend:**
   - Keep previous version tagged in git
   - Can quickly redeploy: `git checkout v1.0 && pm2 restart all`
3. **Database:** No database changes in this tool (testing only)

---

## Cost Estimation

### Minimal Setup (Recommended for Testing)
- Vercel: **Free**
- AWS EC2 t2.micro: **$5/month**
- **Total: $5/month**

### Production Setup
- Vercel: **Free**
- AWS EC2 t2.small or GCP Cloud Run: **$10-20/month**
- Optional monitoring: **$0-10/month**
- **Total: $10-30/month**

### High Traffic Setup
- Vercel: **$20/month (Pro)**
- AWS EC2 t3.medium + Load Balancer: **$50/month**
- Monitoring & Logging: **$20/month**
- **Total: $90/month**

---

## Support

For deployment issues:
- Check [README.md](README.md) for basic setup
- Review [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues
- Check backend logs for API errors
- Test with `curl` commands first

**Last Updated:** 2025-01-15
