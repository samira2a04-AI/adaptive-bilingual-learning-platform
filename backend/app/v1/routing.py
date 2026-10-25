# Adaptive Routing Engine (Week 6 Draft)

Determines the next recommended concept for a student based on:
1. Current mastery estimates (from BKT or other KT models)
2. Prerequisite graph dependencies
3. Bilingual UI language preferences

## Routing Algorithm

```
1. Get current mastery estimates for all concepts the user has interacted with
2. Identify concepts where estimate >= mastery_threshold (default: 0.85) → mastered
3. For each mastered concept, find outgoing edges in the prerequisite graph
4. Collect all dependent concepts (concepts that require the mastered one)
5. Filter out concepts the student has already attempted
6. Rank remaining concepts by:
   a. Number of mastered prerequisites satisfied
   b. Edge strength (hard > soft)
   c. Lower typical_year (earlier concepts first for foundational gaps)
   d. Language preference match
7. Return top-N recommendations
```

## Language-Aware Routing

- User's language preference (AR/EN) is considered when presenting concept names
- Dual-language display: concept name shown in user's preferred language, with alternative
- Routing logic is language-agnostic; only presentation is bilingual

## Priority Rules

| Priority | Rule |
|---|---|
| 1 | Concepts where all hard prerequisites are mastered |
| 2 | Concepts with strongest prerequisite edges (strength=1.0) |
| 3 | Concepts at the lowest typical_year level among candidates |
| 4 | Language preference match for UI display |
| 5 | Recent activity recency boost |

## API Endpoint

```python
POST /api/v1/route/next
Request body:
{
  "user_id": "user_123",
  "current_concept": "M01",  // optional - concept currently being studied
  "exclude_mastered": true,  // optional - whether to exclude already-mastered concepts
  "n_recommendations": 3  // optional - number of recommendations (default: 3)
}

Response:
{
  "user_id": "user_123",
  "recommendations": [
    {
      "concept_id": "M04",
      "concept_name_en": "Variables & Substitution",
      "concept_name_ar": "متغيرات واستstitution",
      "mastery_estimate": 0.92,
      "prerequisites_satisfied": ["M01"],
      "recommended_rationale": "All hard prerequisites (M01) satisfied; foundational algebra concept"
    }
  ],
  "routing_metadata": {
    "algorithm_version": "draft_v1",
    "timestamp": "2026-01-01T00:00:00Z",
    "language": "en"
  }
}
```