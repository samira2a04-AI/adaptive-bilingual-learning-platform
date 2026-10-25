# Concept Schemas (Week 6 Draft)

Based on data-schema_v1.1.md requirements. All schemas support bilingual (AR/EN) labels and versioned knowledge graphs.

## 1. Concepts Table

| Field | Type | Notes |
|-------|------|-------|
| concept_id | PK | Unique identifier (e.g. M01, P05, ML03) |
| name_en | string | English concept name |
| name_ar | string | Arabic concept name (may be transliteration if no native equivalent) |
| description | text | Optional human-readable description |
| domain | enum | Mathematics, Programming, Data, Machine Learning |
| typical_year | integer | Grade/year level when concept is typically introduced |
| kg_version | string | Version of the knowledge graph containing this concept |
| created_at | timestamp | Automated timestamp |

## 2. Concept Prerequisites Table (directed edges)

| Field | Type | Notes |
|-------|------|-------|
| edge_id | PK | Unique identifier |
| concept_id | FK | the dependent concept (the one that requires the prerequisite) |
| prerequisite_concept_id | FK | must be mastered first |
| strength | float | optional weight (0–1); 1 = hard prerequisite, used for routing |
| source | enum | manual / nlp_extracted / curriculum |
| edge_type | enum | hard_prerequisite / soft_related (only hard used for routing) |
| kg_version | string | version of the graph containing this edge |
| annotator_votes / confidence | json / float | agreement evidence for the edge |

Relationship: Concept → Concept (via concept_prerequisites), forming a Directed Acyclic Graph (DAG).

## 3. Lesson Concepts Table (many-to-many link)

| Field | Type | Notes |
|-------|------|-------|
| lesson_id | FK | |
| concept_id | FK | |
| primary | boolean | True if this is the main concept of the lesson |

## 4. Student Concept State Table

| Field | Type | Notes |
|-------|------|-------|
| state_id | PK | |
| user_id | FK | |
| concept_id | FK | |
| estimate | float | 0.0 – 1.0; meaning set by estimate_type (not automatically 'mastery') |
| estimate_type | enum | bkt_p_known / predicted_p_correct / heuristic |
| status | enum | unknown / learning / struggling / mastered (derived by routing rules) |
| model_version_id | FK → kt_model_versions | |
| kg_version | string | graph version used |
| last_updated | timestamp | |
| evidence_count | integer | number of interactions used |
| source_model | string | e.g. BKT, DKT, heuristic |

## 5. KG Versions Table

| Field | Type | Notes |
|-------|------|-------|
| kg_version | PK | e.g. v1.0, v1.1, v2.0 |
| created_at | timestamp | |
| checksum | string | hash of the complete graph state |
| description | string | what changed in this version |

## 6. KT Model Versions Table

| Field | Type | Notes |
|-------|------|-------|
| model_version_id | PK | |
| model_type | enum | BKT, DKT, SAKT, simpleKT, logistic_regression |
| artifact_uri | string | path or URI to trained model |
| config_json | json | model hyperparameters and architecture config |
| training_data_hash | string | hash of the training dataset used |
| kg_version | string | which knowledge graph version was used for training |
| git_commit | string | git commit hash that produced this model |
| metrics_json | json | AUC, log loss, ECE and other evaluation metrics |
| is_active | boolean | whether this version is currently serving |
| created_at | timestamp | |

## 7. Question Translations (bilingual question bank)

| Field | Type | Notes |
|-------|------|-------|
| question_id | FK | same id for AR and EN versions |
| language | enum | ar / en |
| question_text | text | |
| options | json | for MCQ questions |

These schemas are designed to be implemented in a relational database (PostgreSQL recommended) with Prisma or SQLAlchemy ORM. They support the bilingual UI requirement and the longitudinal knowledge graph with versioned edges.