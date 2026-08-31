# Prolixo - Roadmap

## 1. Backend Architecture & Language Generation Engine
### 1.1 Statistical & Context-Free Grammar (CFG) Combinatorial Engine
### 1.2 Multilingual Corpus Integration (Latin, Portuguese, English, Spanish, French)
### 1.3 Specialized Domain Lexicon & Themes (Business, Ecology, Law, Medicine, Mining, Politics, Technology)
### 1.4 Output Format Handlers (Words, Sentences, Paragraphs)
### 1.5 FastAPI REST Endpoints & Schema Validation

## 2. Frontend User Interface & Experience
### 2.1 Next.js App Router Architecture & Tailwind CSS Setup
### 2.2 Accessible UI Controls with Radix UI (Language & Theme Selectors, Mode Tabs, Slider)
### 2.3 Dynamic Text Viewer & Real-Time Copy-to-Clipboard
### 2.4 Light & Dark Mode System Theme Synchronization
### 2.5 About & Inspirations Modal with Historical References

## 3. Design System & Visual Identity
### 3.1 Official Color Palette Definition (Terracotta, Peach Sand, Mint Accent, Charcoal, Pure White)
### 3.2 Full Tonal Color Scales (Steps 50 to 950) in Tailwind Configuration
### 3.3 Global CSS Variables & Adaptive Element Theming

## 4. Branding, Iconography & Asset Generation
### 4.1 Official Vector Icon & Brand Mark Design
### 4.2 Web App Favicon & Header SVG Integration
### 4.3 Multi-Resolution Raster PNG Generation (Favicons, Touch Icons, Chrome Assets)
### 4.4 Workspace Cleanup & Production Build Verification

## 5. Linguistic Precision & Quality Noise Injection (NLP / Spellchecker Testing)
### 5.1 Deduplication & Contraction Collision Sanitization (Error-Free Mode)
- Automated consecutive duplicate word collapse (e.g. eliminating accidental "a a", "mínimo mínimo", etc.).
- Preposition-article collision resolution across Romance language dictionaries.
### 5.2 Deterministic Error Injection Engine (`noise.py`)
- **Grammatical Noise Engine**: Synthetic insertion of grammatical token duplications, subject-verb disagreement, and number/gender mismatches across PT, EN, ES, and FR inspired by LanguageTool rules.
- **Orthographical Noise Engine**: Realistic spelling corruptions, diacritic drops, and phonetic/transposition mutations (e.g., `length`/`lenght`, `height`/`heigth`, `width`/`widht`, `ei`/`ie`, `ss`/`ç`, `concerteza`, `excessão`, `dévelopement`, etc.).
### 5.3 Classical Latin (*Lorem Ipsum*) Domain Isolation
- Classical Markov Order-2 generator execution bypassing domain themes and error injection.
- UI state guards: automatic disabling of Theme dropdown (showing `-`) and Linguistic Precision switches with `cursor-not-allowed` indicator.
### 5.4 Sidebar Linguistic Precision Controls & Interactive Tooltips
- Stacked independent switches for **Grammar** and **Orthography** with Thumbs Up / Down indicators.
- Explanatory information tooltip on the **Linguistic Precision** header detailing NLP/spellchecker testing use cases.

