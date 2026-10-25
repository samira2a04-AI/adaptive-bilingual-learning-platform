# Project Overview

## Adaptive Bilingual Learning Platform Pilot

**Pilot Objective:** Evaluate an adaptive bilingual learning system that personalizes educational content based on student knowledge and language proficiency while maintaining human-in-the-loop governance.

**Core Principle:** "AI assists, humans decide." All system recommendations are presented as reviewable suggestions subject to human validation and override.

**Pilot Source:** Google Machine Learning Crash Course (MLCC). Selected modules inform knowledge modeling, adaptive routing, and evaluation design.

**Pilot Scope:**
- Knowledge concept graph construction with prerequisite dependencies
- Basic adaptive routing based on mastery state and prerequisites
- Bilingual UI with language selection and dual-language content presentation
- Ethics and consent framework for data privacy and bias mitigation
- MLCC-aligned evaluation metrics (AUC, accuracy, log loss)

**Out of Scope:** Automated student grading, irreversible progression decisions, confidential assessment data processing.

**Workstreams:**
1. Knowledge Modeling - concept taxonomy, prerequisite graph, mastery representation
2. Backend and Data - API design, data pipeline, state management
3. Ethics and Consent - data privacy, informed consent, bias mitigation
4. Bilingual UI - language switching, locale-aware adaptive routing

**Repository Structure:** See README.md at repository root for the full directory layout.

**Current Status:** 
- Knowledge model: 73 concepts in 4 layers with prerequisite graph (v1.0)
- Backend: FastAPI foundation with BKT model, routing, and API endpoints
- Frontend: React bilingual UI with language switching and concept browser
- Ethics framework: Full governance document with bias audit protocol
- Evaluation framework: AUC/accuracy/log loss metrics with bilingual UI assessment
- All workstreams: Implementation complete; ready for pilot testing