# Student Dashboard (Week 6 Draft)

React component displaying the student's mastery breakdown across all concepts, with adaptive routing recommendations and bilingual concept presentation.

## Sections

### Mastery Overview

Radial/summary chart showing overall mastery distribution across 4 layers:
- Mathematics: X% mastery
- Programming: Y% mastery
- Data: Z% mastery
- ML Core: W% mastery

### Concept-wise Breakdown

List of all 73 concepts with:
- Concept ID (e.g., M01, P05, ML03)
- Concept name in user's preferred language (AR/EN)
- Mastery estimate (0.0 – 1.0) from BKT model
- Status: unknown / learning / struggling / mastered
- Prerequisite circles: which pre-requisites are satisfied ❌/✓
- "Ready to learn" indicator when all hard prerequisites are mastered

### Adaptive Recommendations

Top 3 next concepts based on routing engine:
- Concept ID and name (bilingual display)
- Mastery estimate
- Rationale (which prerequisites were satisfied)
- Start learning button

### Language Toggle

Inline language switcher within dashboard for switching between AR and EN display without leaving the page.

## API Integration

- Fetches mastery estimates from `GET /api/v1/mastery/{user_id}`
- Gets routing recommendations from `POST /api/v1/route/next`
- Updates language via `POST /api/v1/ui/language/{user_id}`