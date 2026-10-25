# Frontend App (Week 6 Draft)

Main application component for the Adaptive Bilingual Learning Platform frontend. Sets up routing, context providers, and page layout.

## Routes

| Path | Component | Description |
|---|---|---|
| `/` | `Dashboard` | Student dashboard with mastery overview and recommendations |
| `/concepts` | `ConceptBrowser` | Knowledge graph browser with bilingual display |
| `/login` | `Login` | User login and language selection |
| `/profile` | `Profile` | User profile and consent management |

## Layout

- Top language navigation bar (BilingualContext provider)
- Sidebar with layer navigation (for ConceptBrowser)
- Main content area with route-matched component
- Footer with ethics and consent links

## Providers

- `BilingualContext` - Language state management
- `AuthContext` - User authentication state (placeholder for future work)
- `RouterProvider` - React Router navigation

## Styling

- CSS Modules or Tailwind CSS for responsive design
- Arabic language support (direction: rtl for ar language, ltr for en)
- High contrast mode for accessibility