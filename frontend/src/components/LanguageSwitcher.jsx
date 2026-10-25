# Language Switcher (Week 6 Draft)

React component for language selection and switching in the Adaptive Bilingual Learning Platform frontend.

## Features

- Toggle between Arabic (ar) and English (en) language preferences
- Display current language with flag icons or language abbreviations
- Persist selection via BilingualContext
- Accessible with keyboard support

## Props

| Prop | Type | Description |
|---|---|---|
| `language` | `"en" | "ar"` | Current selected language |
| `onChange` | `(lang: "en" | "ar") => void` | Callback when language changes |
| `showFlags` | `boolean` | Whether to show Arabic/English flag icons (default: true) |

## Example

```jsx
<LanguageSwitcher
  language={currentLanguage}
  onChange={setLanguage}
/>
```

## Language Map

| Code | Label | Flag |
|---|---|---|
| `"en"` | English | 🇺🇸 |
| `"ar"` | Arabic | 🇦🇪 |