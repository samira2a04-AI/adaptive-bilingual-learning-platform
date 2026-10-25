# App Main Entry Point (Week 6 Draft)

FastAPI application master file for the Adaptive Bilingual Learning Platform.

## Configuration

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.v1 import router as v1_router

app = FastAPI(
    title="Adaptive Bilingual Learning Platform API",
    description="API for adaptive bilingual learning system with human-in-the-loop governance",
    version="0.1.0",
)

# CORS - configure for production origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include v1 API router
app.include_router(v1_router, prefix="/api/v1", tags=["v1"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "adaptive-bilingual-learning-platform"}

# Version endpoint
@app.get("/version")
async def version():
    return {"version": "0.1.0", "kg_version": "v1.0", "model": "BKT"}