# Frontend Directory

Bilingual user interface for the adaptive learning platform.

**Features:**
- Language selection and switching (Arabic/English)
- Dual-language content presentation with bilingual concept names
- Adaptive routing based on concept mastery estimates
- Concept graph visualization with status color coding
- Student dashboard with mastery breakdown per concept
- Language preference persistence via localStorage

**Key Components:**
- `BilingualContext` - React context for language state management
- `LanguageSwitcher` - Language toggle component
- `Dashboard` - Student mastery overview and recommendations
- `ConceptBrowser` - Knowledge graph visualization

**Workstream:** Integrates with backend APIs and knowledge model for adaptive recommendations and bilingual presentation.

**Frontend Structure:**
- `src/components/` - Reusable UI components
- `src/pages/` - Page-level components (Dashboard, ConceptBrowser)
- `src/context/BilingualContext.jsx` - Language state management
- `src/utils/` - Utility functions for API calls and formatting