# Backend Directory

API server and data processing service for the adaptive bilingual learning platform.

**Technology Stack:** FastAPI (Python) with SQLAlchemy ORM, BKT/DKT implementation, Pydantic models.

**Endpoints:**

| Category | Endpoints |
|---|---|
| Mastery | `GET /api/v1/mastery/{user_id}/{concept_id}`, `POST /api/v1/mastery/predict` |
| Concept Graph | `GET /api/v1/graph`, `GET /api/v1/graph/prerequisites/{concept_id}` |
| Routing | `POST /api/v1/route/next`, `GET /api/v1/route/path/{user_id}` |
| Bilingual UI | `GET /api/v1/ui/language/{user_id}`, `POST /api/v1/ui/language/{user_id}` |
| Ethics | `POST /api/v1/ethics/consent`, `GET /api/v1/ethics/audit/{user_id}`, `POST /api/v1/ethics/bias-check` |

**Workstream:** Coordinates with knowledge modeling for data flow and with ethics for data privacy controls.

**Backend Structure:**
- `app/main.py` - FastAPI application entry point
- `app/v1/` - API v1 routes (mastery, graph, routing, bilingual, ethics)
- `app/models/` - Pydantic models aligned with knowledge-model schemas
- `app/models/bkt.py` - Bayesian Knowledge Tracing implementation