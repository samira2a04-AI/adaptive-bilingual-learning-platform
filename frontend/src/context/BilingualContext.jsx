# Bilingual Context (Week 6 Draft)

React Context for managing user language preference and dual-language content state across the Adaptive Bilingual Learning Platform frontend.

## Context Value

```javascript
{
  language: "en" | "ar",     // User's selected language preference
  setLanguage: (lang: "en" | "ar") => void,  // Update language preference
  userId: string,            // Current user identifier
  conceptLanguage: "en" | "ar",  // Language for concept display
  setConceptLanguage: (lang: "en" | "ar") => void  // Per-concept language override
}
```

## Usage

```javascript
import { BilingualContext } from "../context/BilingualContext";

function Component() {
  const { language, setLanguage, conceptLanguage, setConceptLanguage } = useContext(BilingualContext);
  
  return (
    <div>
      <LanguageSwitcher language={language} onChange={setLanguage} />
      <ConceptDisplay language={conceptLanguage} />
    </div>
  );
}
```

## Persistence

Language preference persisted to localStorage with key `bilingual_language` for session restore.