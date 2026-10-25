# Backend API v1 (Week 6 Draft)

Router for the Adaptive Bilingual Learning Platform API v1. Includes endpoints for mastery prediction, concept graph queries, adaptive routing, and bilingual state management.

## FastAPI Router Integration

```python
from fastapi import APIRouter, Depends, HTTPException
from app.v1 import router as v1_router

app.include_router(v1_router, prefix="/api/v1", tags=["v1"])
```

## Endpoint Summary

| Category | Endpoints |
|---|---|
| Mastery | `GET /mastery/{user_id}/{concept_id}`, `POST /predict` |
| Graph | `GET /graph`, `GET /prerequisites/{concept_id}`, `GET /valid-path/{user_id}` |
| Routing | `POST /route/next`, `GET /route/path/{user_id}` |
| UI Language | `GET /ui/language/{user_id}`, `POST /ui/language/{user_id}` |
| Ethics | `POST /ethics/consent`, `GET /audit/{user_id}`, `POST /bias-check` |