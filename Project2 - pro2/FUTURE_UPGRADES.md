# Future Upgrades Tracker

> **Purpose:** Track all planned enhancements for upgrading from prototype to production RAG system  
> **Last Updated:** 2026-01-06  
> **Project:** Research Compass - Multi-Agent RAG System

---

## 🎯 Vision

Transform current API-heavy prototype into a **cloud-native, progressive knowledge base RAG system** with Google Vertex AI integration.

---

## 📋 Phase 1: Enhanced Local Prototype (THIS MONTH)

### 1.1 Progressive Knowledge Base
**Priority:** 🔴 CRITICAL  
**Status:** ⏳ PENDING  
**Estimated Time:** 3-4 days

#### Tasks:
- [ ] Design database schema for papers metadata
- [ ] Create `database/papers_store.py` module
- [ ] Implement paper storage with deduplication (by DOI)
- [ ] Add metadata tracking: source, fetch timestamp, authors, venue
- [ ] Update search agent to check local KB first

**Schema Design:**
```sql
CREATE TABLE papers (
    id INTEGER PRIMARY KEY,
    doi TEXT UNIQUE,
    title TEXT NOT NULL,
    abstract TEXT,
    authors TEXT,  -- JSON array
    year INTEGER,
    venue TEXT,
    source TEXT,   -- 'springer', 'semanticscholar'
    url TEXT,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    access_count INTEGER DEFAULT 0
);

CREATE INDEX idx_doi ON papers(doi);
CREATE INDEX idx_year ON papers(year);
CREATE INDEX idx_source ON papers(source);
```

---

### 1.2 Local Vector Store
**Priority:** 🔴 CRITICAL  
**Status:** ⏳ PENDING  
**Estimated Time:** 2-3 days

#### Tasks:
- [ ] Create `database/vector_store.py` module
- [ ] Implement NumPy-based embedding cache
- [ ] Build vector similarity search (FAISS or pure NumPy)
- [ ] Link embeddings to paper IDs
- [ ] Add incremental embedding storage

**File Structure:**
```
data/
├── embeddings/
│   ├── vectors.npy      # All embedding vectors
│   ├── index.json       # {paper_id: vector_index}
│   └── metadata.json    # Embedding model info
```

---

### 1.3 Smart Multi-Level Caching
**Priority:** 🟡 HIGH  
**Status:** ⏳ PENDING  
**Estimated Time:** 1-2 days

#### Tasks:
- [ ] Implement query result cache with TTL
- [ ] Cache summary results separately
- [ ] Add cache warming for popular queries
- [ ] Implement LRU eviction policy
- [ ] Add cache statistics tracking

**Cache Layers:**
```python
# Level 1: Query → Paper IDs (TTL: 1 hour)
# Level 2: Paper ID → Summary (TTL: 7 days)
# Level 3: Query → Final Answer (TTL: 24 hours)
```

---

### 1.4 Updated Retrieval Flow
**Priority:** 🔴 CRITICAL  
**Status:** ⏳ PENDING  
**Estimated Time:** 2 days

#### Tasks:
- [ ] Implement local-first retrieval logic
- [ ] Add confidence threshold for local results
- [ ] Fallback to API only when needed
- [ ] Store all API results in local KB
- [ ] Add retrieval analytics

**New Flow:**
```
Query → Check Cache → Check Local KB → API Call (if needed) → Store → Rank → Generate
```

---

### 1.5 Database Migration Tool
**Priority:** 🟢 MEDIUM  
**Status:** ⏳ PENDING  
**Estimated Time:** 1 day

#### Tasks:
- [ ] Create migration script from current SQLite cache
- [ ] Build data import/export tools
- [ ] Add backup functionality
- [ ] Create database reset tool for testing

---

### 1.6 Performance & Monitoring
**Priority:** 🟢 MEDIUM  
**Status:** ⏳ PENDING  
**Estimated Time:** 1-2 days

#### Tasks:
- [ ] Add structured logging (Python `logging` module)
- [ ] Track retrieval metrics (cache hits, API calls, latency)
- [ ] Create `/health` endpoint for app status
- [ ] Add `/metrics` endpoint (optional)
- [ ] Implement request timing middleware

---

## 📋 Phase 2: Cloud Migration (NEXT 2-3 MONTHS)

### 2.1 Google Cloud Platform Setup
**Priority:** 🟡 HIGH  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 1 week

#### Tasks:
- [ ] Create GCP project
- [ ] Enable billing (get $300 free credit)
- [ ] Enable required APIs:
  - [ ] Vertex AI API
  - [ ] Cloud SQL Admin API
  - [ ] Cloud Run API
  - [ ] Cloud Memorystore (Redis) API
  - [ ] Secret Manager API
- [ ] Set up IAM roles and service accounts
- [ ] Configure VPC and networking

---

### 2.2 Vertex AI Integration
**Priority:** 🔴 CRITICAL  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 1-2 weeks

#### Tasks:
- [ ] Replace Gemini Embeddings with Vertex AI Text Embedding
- [ ] Migrate from Groq to Vertex AI PaLM 2 / Gemini Pro
- [ ] Update `ai_config.py` for Vertex AI SDK
- [ ] Test embedding compatibility
- [ ] Implement retry logic for Vertex AI

**Vertex AI Components:**
```python
# Embeddings: textembedding-gecko@003
# LLM: gemini-pro or chat-bison
```

---

### 2.3 Cloud SQL Migration
**Priority:** 🔴 CRITICAL  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 3-5 days

#### Tasks:
- [ ] Provision Cloud SQL (PostgreSQL) instance
- [ ] Migrate schema from SQLite to PostgreSQL
- [ ] Update database connection logic
- [ ] Implement connection pooling
- [ ] Configure automatic backups
- [ ] Set up read replicas (optional)

---

### 2.4 Vertex AI Vector Search
**Priority:** 🔴 CRITICAL  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 1 week

#### Tasks:
- [ ] Create Vertex AI Matching Engine index
- [ ] Migrate embeddings from NumPy to Vector Search
- [ ] Implement index updates (add new papers)
- [ ] Configure similarity search parameters
- [ ] Test query performance vs local search

---

### 2.5 Cloud Memorystore (Redis)
**Priority:** 🟡 HIGH  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 2-3 days

#### Tasks:
- [ ] Provision Memorystore Redis instance
- [ ] Migrate cache logic from SQLite to Redis
- [ ] Implement Redis-based query cache
- [ ] Set up TTL policies
- [ ] Add cache monitoring

---

### 2.6 Cloud Run Deployment
**Priority:** 🔴 CRITICAL  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 3-5 days

#### Tasks:
- [ ] Create `Dockerfile` for Flask app
- [ ] Build and test Docker container locally
- [ ] Deploy to Cloud Run
- [ ] Configure service account permissions
- [ ] Set up environment variables via Secret Manager
- [ ] Configure auto-scaling policies
- [ ] Set up custom domain (optional)

---

### 2.7 CI/CD Pipeline
**Priority:** 🟢 MEDIUM  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 2-3 days

#### Tasks:
- [ ] Set up Cloud Build triggers
- [ ] Create build configuration (`cloudbuild.yaml`)
- [ ] Implement automated testing in CI
- [ ] Configure staging environment
- [ ] Implement blue-green deployment
- [ ] Add rollback mechanism

---

### 2.8 Monitoring & Alerting
**Priority:** 🟡 HIGH  
**Status:** ⏳ NOT STARTED  
**Estimated Time:** 2-3 days

#### Tasks:
- [ ] Set up Cloud Monitoring dashboards
- [ ] Configure error reporting
- [ ] Add custom metrics (cache hit rate, API calls, etc.)
- [ ] Set up alerting policies
- [ ] Implement logging aggregation
- [ ] Create uptime checks

---

## 📋 Phase 3: Production Enhancements (LATER)

### 3.1 User Authentication
**Priority:** 🟢 MEDIUM  
**Status:** ⏳ NOT STARTED

#### Tasks:
- [ ] Implement Firebase Auth or Cloud Identity Platform
- [ ] Add user session management
- [ ] Track user-specific search history
- [ ] Implement usage quotas per user

---

### 3.2 Advanced Features
**Priority:** 🔵 LOW  
**Status:** ⏳ NOT STARTED

#### Tasks:
- [ ] Paper recommendation system
- [ ] Citation network visualization
- [ ] Export results to PDF/BibTeX
- [ ] Collaborative research folders
- [ ] Email alerts for new papers

---

### 3.3 Multi-Source Expansion
**Priority:** 🟢 MEDIUM  
**Status:** ⏳ NOT STARTED

#### Tasks:
- [ ] Add arXiv API integration
- [ ] Add PubMed API integration
- [ ] Add IEEE Xplore API
- [ ] Implement source priority weighting

---

### 3.4 Performance Optimization
**Priority:** 🟡 HIGH  
**Status:** ⏳ NOT STARTED

#### Tasks:
- [ ] Implement query result prefetching
- [ ] Add CDN for static assets
- [ ] Optimize database queries
- [ ] Implement batch processing for embeddings
- [ ] Add response caching at edge (Cloud CDN)

---

## 🛠️ Technical Debt

### Code Quality
- [ ] Add comprehensive unit tests (pytest)
- [ ] Add integration tests
- [ ] Implement type hints throughout codebase
- [ ] Add API documentation (Swagger/OpenAPI)
- [ ] Code coverage > 80%

### Security
- [ ] Implement rate limiting per IP
- [ ] Add input validation and sanitization
- [ ] Use parameterized queries (SQL injection prevention)
- [ ] Implement CORS properly
- [ ] Add API authentication

### Documentation
- [ ] Complete API documentation
- [ ] Add deployment guide
- [ ] Create architecture diagrams
- [ ] Document all environment variables
- [ ] Add troubleshooting guide

---

## 📊 Success Metrics to Track

| Metric | Current | Phase 1 Goal | Phase 2 Goal |
|--------|---------|--------------|--------------|
| **Response Time** | 5-10s | 2-5s | 1-3s |
| **Cache Hit Rate** | ~20% | 60% | 85% |
| **API Calls/Query** | 1-2 | 0-1 | 0-1 |
| **Papers in KB** | 0 | 500+ | 10,000+ |
| **Uptime** | N/A | Local | 99.5% |
| **Cost/Month** | $0 | $0 | <$150 |

---

## 🔗 Resources & Links

### Google Cloud Documentation
- [Vertex AI Overview](https://cloud.google.com/vertex-ai/docs)
- [Cloud Run Quickstart](https://cloud.google.com/run/docs/quickstarts)
- [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres)
- [Vertex AI Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/overview)
- [Cloud Memorystore for Redis](https://cloud.google.com/memorystore/docs/redis)

### Learning Resources
- [ ] Complete Vertex AI codelab
- [ ] Review Cloud Run best practices
- [ ] Study RAG architecture patterns
- [ ] Learn PostgreSQL optimization

---

## 📝 Notes & Decisions

### 2026-01-06
- Decided on progressive KB approach (not full ingestion)
- Chose Google Vertex AI for cloud deployment
- Will implement Phase 1 locally before cloud migration
- Targeting Cloud Run for initial deployment (not App Engine)

---

## 🚀 Quick Reference

### Start Phase 1
```bash
# Create new branches
git checkout -b feature/progressive-kb
git checkout -b feature/vector-store
git checkout -b feature/smart-cache
```

### Before Phase 2
```bash
# Set up GCP
gcloud init
gcloud config set project YOUR_PROJECT_ID
gcloud services enable aiplatform.googleapis.com
```

---

**Remember:** You're not building Google Scholar. You're building an intelligent assistant that learns from actual usage. Start small, grow organically! 🌱
