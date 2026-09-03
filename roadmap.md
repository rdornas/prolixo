# Prolixo - Roadmap

## 1. Backend Architecture & Language Generation Engine
### 1.1 Statistical & Context-Free Grammar (CFG) Combinatorial Engine
### 1.2 Multilingual Corpus Integration (Latin, Portuguese, English, Spanish, French)
### 1.3 Specialized Domain Lexicon & Themes (Business, Ecology, Law, Medicine, Mining, Politics, Technology)
- High-register specialized vocabulary decks for 7 key professional domains in PT, EN, ES, and FR.
- Theme-specific circumstantial intro deck isolation (`circ`) ensuring domain purity across generations.
### 1.4 Output Format Handlers (Words, Sentences, Paragraphs)
### 1.5 FastAPI REST Endpoints & Schema Validation

## 2. Frontend User Interface & Experience
### 2.1 Next.js App Router Architecture & Tailwind CSS Setup
### 2.2 Accessible UI Controls with Radix UI (Language & Theme Selectors, Mode Tabs, Slider)
- Dynamic non-intrusive scroll affordance and smooth native scrolling for theme and language dropdowns with subtle overlay gradients, custom scrollbar styling, and dynamic arrow indicators (`ScrollableSelectContent`).
### 2.3 Dynamic Text Viewer & Real-Time Copy-to-Clipboard
### 2.4 Light & Dark Mode System Theme Synchronization
### 2.5 About & Inspirations Modal with Historical References
### 2.6 Metadata Diagnostics & Character Count
- Real-time generation timestamp display (`Generated at: ...`) and complete character count tracking (including spaces and punctuation).
- Manual placeholder generation trigger alignment preventing premature rendering on configuration changes.
### 2.7 Navigation & Documentation Integration
- Official circular GitHub repository navigation link integrated into the header alongside theme controls with brand color hover states.
- Interactive Swagger API Documentation link (`/api/docs`) placed directly in the footer with `<Code2 />` icon.
- Dynamic development port resolution (`scripts/find_ports.py`) preventing port collisions on `make run-local`.
### 2.8 Custom Selection Styling & Real-Time Character Counter (Generated Text Scope)
- Scoped subtle selection background (`rgba(186, 90, 49, 0.03)` Terra 500 at 3% opacity) with primary brand Terra 500 text styling (`#ba5a31` on both light and dark) applied exclusively to generated text blocks (`.generated-text-content`), preserving default system selection for UI chrome and controls.
- Floating real-time character count tooltip scoped strictly to the generated text viewer with active caret/cursor directional tracking (following top-to-bottom and bottom-to-top selections seamlessly).
- Integrated inline copy button (`<Copy />` / `<Check />`) copying exclusively the highlighted text segment without breaking the active DOM selection.

## 3. Design System & Visual Identity
### 3.1 Official Color Palette Definition (Terracotta, Peach Sand, Mint Accent, Charcoal, Pure White)
### 3.2 Full Tonal Color Scales (Steps 50 to 950) in Tailwind Configuration
### 3.3 Global CSS Variables & Adaptive Element Theming

## 4. Branding, Iconography & Asset Generation
### 4.1 Official Vector Icon & Brand Mark Design
### 4.2 Web App Favicon & Header SVG Integration
### 4.3 Multi-Resolution Raster PNG Generation (Favicons, Touch Icons, Chrome Assets)
### 4.4 Workspace Cleanup & Production Build Verification
### 4.5 Open Graph & Social Preview Cards (WhatsApp, Teams, Slack, Twitter/X)
- Standardized `1200 x 630 px` rich preview image asset (`frontend/src/app/opengraph-image.png`) with Prolixo branding and high contrast typography.
- Next.js App Router `metadataBase` configuration and automated `og:image` / `twitter:image` HTML tag generation.

## 5. Linguistic Precision & Quality Noise Injection (NLP / Spellchecker Testing)
### 5.1 Deduplication, Whitespace & Contraction Collision Sanitization (Error-Free Mode)
- Automated consecutive duplicate word collapse (e.g. eliminating accidental "a a", "mínimo mínimo", etc.).
- Robust multi-space and punctuation spacing sanitization (`re.sub`) across all CFG structural productions (e.g., circumstance intro clauses).
- Preposition-article and preposition-demonstrative collision resolution across Romance languages (`destes`, `neste`, `daquele`, `del`, `du`, `au`, etc.).
- Strict gender taxonomy validation across specialized domain lexicons (e.g., feminine mining nouns like *"rocha encaixante"*).
- Conciseness sanitization on formal introductions (e.g., replacing verbose *"Para além disso"* with concise *"Além disso"*).
### 5.2 Deterministic Error Injection Engine (`noise.py`)
- **Grammatical Noise Engine**: Synthetic insertion of grammatical token duplications, subject-verb disagreement, number/gender mismatches, and stylistic/prolix redundancies (*"Para além disso"*) across PT, EN, ES, and FR inspired by LanguageTool rules.
- **Orthographical Noise Engine**: Realistic spelling corruptions, diacritic drops, and phonetic/transposition mutations (e.g., `length`/`lenght`, `height`/`heigth`, `width`/`widht`, `ei`/`ie`, `ss`/`ç`, `concerteza`, `excessão`, `dévelopement`, etc.).
### 5.3 Classical Latin (*Lorem Ipsum*) Domain Isolation
- Classical Markov Order-2 generator execution bypassing domain themes and error injection.
- UI state guards: automatic disabling of Theme dropdown (showing `-`) and Linguistic Precision switches with `cursor-not-allowed` indicator.
### 5.4 Sidebar Linguistic Precision Controls & Interactive Tooltips
- Stacked independent switches for **Grammar** and **Orthography** with Thumbs Up / Down indicators.
- Explanatory information tooltip on the **Linguistic Precision** header detailing NLP/spellchecker testing use cases.

## 6. Automated Testing & TDD Suite
### 6.1 Backend Generator & API Test Suite (`pytest`)
- Exhaustive test suite covering CFG grammar engines, Markov generation, deck shuffling, stemmers, noise injection, and FastAPI endpoint schemas.
- Integrated `make test` automated test target with sub-second feedback (~0.2s).
- Pre-push documentation sync and verification workflow.

## 7. Cloud Deployment & Production Hosting (Vercel)
### 7.1 Multi-Service Vercel Deployment Specification (`vercel.json`)
- Multi-service deployment routing Next.js (`frontend/`) and FastAPI (`api/app/main.py`).
- Relative API base proxy configuration in Next.js development and production rewrites.

## 8. Request Rate Limiting & Origin-Aware Abuse Prevention
### 8.1 In-Memory Zero-Dependency Sliding Window Limiter (`limiter.py`)
- Independent sliding window rate tracking with zero third-party dependencies.
- Origin differentiation: trusted frontend traffic vs. direct external API/script traffic.
- Transparent proxy IP extraction supporting `X-Forwarded-For` and `X-Forwarded-User-IP`.
- Standard HTTP 429 status code, structured JSON response body, and `Retry-After` header.
### 8.2 Frontend Abuse Notice & Rate Limit Alert
- Frontend rate limit feedback banner with dynamic `Retry-After` wait notice and user-friendly error recovery.




