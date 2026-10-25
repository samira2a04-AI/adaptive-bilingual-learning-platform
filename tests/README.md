# Tests Directory

Test suite for the adaptive bilingual learning platform.

**Test Categories:**

| Category | Description | Implementation |
|---|---|---|
| Unit tests for knowledge model components | Concept schemas, prerequisite graph integrity, bilingual label validation | Jest/Mocha test suites |
| Integration tests for backend API endpoints | Mastery prediction, graph queries, routing recommendations, bilingual state management | Supertest + Mocha |
| Frontend component tests for bilingual UI | Language switcher, concept display, dashboard interactions | React Testing Library |
| End-to-end tests for adaptive routing workflows | Full routing cycle: interaction → mastery update → recommendation → student response | Cypress with fixtures |

**Test Data fixtures:** Use synthetic data with known BKT parameters; no real student data.

**Test Ethics:** All tests respect the ethics framework - no PII in test data, consent mocks where needed, bias checks included in CI pipeline.

**Workstream:** Coordinates with all other workstreams to ensure system correctness and ethics compliance.