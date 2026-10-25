# Backend API Routes (Week 6 Draft)

Core route implementations for the Adaptive Bilingual Learning Platform backend.

## Registered Routes

| Blueprint | Prefix | Tags |
|---|---|---|
| `/mastery` | `/api/v1/mastery` | ["mastery"] |
| `/graph` | `/api/v1/graph` | ["graph"] |
| `/route` | `/api/v1/route` | ["routing"] |
| `/ui` | `/api/v1/ui` | ["bilingual"] |
| `/ethics` | `/api/v1/ethics` | ["ethics"] |

## Key Route Summaries

### Mastery Routes
- `GET /mastery/{user_id}/{concept_id}` - Returns current BKT mastery estimate and status
- `POST /predict` - Updates mastery estimate based on response (correct/incorrect)

### Graph Routes
- `GET /graph` - Returns complete KG version, concept list, and edge list
- `GET /prerequisites/{concept_id}` - Returns all prerequisite edges for a concept

### Routing Routes
- `POST /route/next` - Returns next concept recommendation for a user
- `GET /route/path/{user_id}` - Returns complete learning path

### Bilingual UI Routes
- `GET /ui/language/{user_id}` - Returns user's language preference (ar/en)
- `POST /ui/language/{user_id}` - Updates user language preference

### Ethics Routes
- `POST /ethics/consent` - Records user consent status and timestamp
- `GET /audit/{user_id}` - Returns ethics audit log for user