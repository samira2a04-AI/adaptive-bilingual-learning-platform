# Backend Models (Week 6 Draft)

Pydantic models aligned with knowledge-model/schemas concept_schemas.md. Supports bilingual (AR/EN) labels and versioned knowledge graphs.

## Concept Schemas

```python
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from typing import Optional, Literal

class Domain(str, Enum):
    Mathematics = "Mathematics"
    Programming = "Programming"
    Data = "Data"
    MachineLearning = "MachineLearning"

class EstimateType(str, Enum):
    bkt_p_known = "bkt_p_known"
    predicted_p_correct = "predicted_p_correct"
    heuristic = "heuristic"

class Status(str, Enum):
    unknown = "unknown"
    learning = "learning"
    struggling = "struggling"
    mastered = "mastered"

class QuestionLanguage(str, Enum):
    ar = "ar"
    en = "en"

class KGVersionBase(BaseModel):
    kg_version: str = Field(..., description="Version of the knowledge graph (e.g. v1.0, v1.1)")
    description: Optional[str] = Field(None, description="What changed in this version")
    checksum: Optional[str] = Field(None, description="Hash of the complete graph state")

class ConceptBase(BaseModel):
    concept_id: str = Field(..., description="Unique identifier (e.g. M01, P05, ML03)")
    name_en: str = Field(..., description="English concept name")
    name_ar: str = Field(..., description="Arabic concept name (transliteration if no native equivalent)")
    description: Optional[str] = Field(None, description="Human-readable description")
    domain: Domain = Field(..., description="Mathematics, Programming, Data, Machine Learning")
    typical_year: int = Field(..., description="Grade/year level when concept is typically introduced")
    kg_version: str = Field(..., description="Version of the knowledge graph containing this concept")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Automated timestamp")

class ConceptPrerequisiteBase(BaseModel):
    edge_id: str = Field(..., description="Unique identifier")
    concept_id: str = Field(..., description="The dependent concept (the one that requires the prerequisite)")
    prerequisite_concept_id: str = Field(..., description="Must be mastered first")
    strength: float = Field(1.0, ge=0, le=1, description="Optional weight; 1 = hard prerequisite, used for routing")
    source: str = Field("manual", description="manual / nlp_extracted / curriculum")
    edge_type: str = Field("hard_prerequisite", description="hard_prerequisite / soft_related (only hard used for routing)")
    kg_version: str = Field(..., description="Version of the graph containing this edge")
    annotator_votes: Optional[float] = Field(None, description="Agreement evidence for the edge")

class StudentConceptStateBase(BaseModel):
    state_id: str = Field(..., description="Unique identifier")
    user_id: str = Field(..., description="User identifier")
    concept_id: str = Field(..., description="Concept identifier")
    estimate: float = Field(0.0, ge=0.0, le=1.0, description="0.0 – 1.0; meaning set by estimate_type")
    estimate_type: EstimateType = Field(EstimateType.bkt_p_known, description="bkt_p_known / predicted_p_correct / heuristic")
    status: Status = Field(Status.unknown, description="unknown / learning / struggling / mastered (derived by routing rules)")
    model_version_id: Optional[str] = Field(None, description="FK → kt_model_versions")
    kg_version: str = Field(..., description="Graph version used")
    last_updated: datetime = Field(default_factory=datetime.utcnow, description="")
    evidence_count: int = Field(0, ge=0, description="Number of interactions used")
    source_model: str = Field("BKT", description="e.g. BKT, DKT, heuristic")

class KGVersionRead(KGVersionBase):
    created_at: datetime
    class Config:
        from_attributes = True

class StudentConceptStateRead(StudentConceptStateBase):
    state_id: str
    class Config:
        from_attributes = True

class QuestionTranslationBase(BaseModel):
    question_id: str = Field(..., description="Same id for AR and EN versions")
    language: QuestionLanguage = Field(..., description="ar / en")
    question_text: str = Field(..., description="")
    options: Optional[dict] = Field(None, description="For MCQ questions")

class QuestionTranslationRead(QuestionTranslationBase):
    language_id: str
    class Config:
        from_attributes = True