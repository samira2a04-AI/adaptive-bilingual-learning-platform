# Concept Browser (Week 6 Draft)

React page displaying the knowledge graph with bilingual concept presentation and prerequisite relationship visualization.

## Features

### Bilingual Concept List

- Toggle between Arabic and English concept names
- Search/filter concepts by ID, name, or domain
- Pagination for full 73-concept list

### Graph Visualization

- Directed graph showing concept-prerequisite relationships
- Node color coding by mastery status:
  - Gray: unknown
  - Blue: learning
  - Orange: struggling
  - Green: mastered
- Edge direction: from prerequisite → dependent
- Edge strength: line thickness (stronger = harder prerequisite)
- Hover tooltip with concept description and year level

### Layer Navigation

- Tabbed interface for 4 layers:
  - Mathematics (M01-M22)
  - Programming (P01-P20)
  - Data (D01-D15)
  - ML Core (ML01-ML16)

### Cross-Layer Connections

- Highlight edges that cross layer boundaries
- Show conceptual dependencies between domains (e.g., ML14 → P13 for recursion in ML)

### Interactive Features

- Click a concept → show mastery estimate and status
- Click a prerequisite edge → show edge details (strength, source)
- "Show prerequisites" / "Show dependents" toggle for any concept
- "Find learning path" from root to target concept