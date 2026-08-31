"use client";

import React, { useState, useEffect, useCallback } from "react";
import * as Tabs from "@radix-ui/react-tabs";
import * as Select from "@radix-ui/react-select";
import * as Slider from "@radix-ui/react-slider";
import { ChevronDown, ChevronUp, Copy, Check, Sparkles, RefreshCw, Languages, FileText, AlignLeft, Type, Sun, Moon, Info, X, Github, ThumbsUp, ThumbsDown, SpellCheck } from "lucide-react";

interface Language {
  code: string;
  name: string;
}

const LANGUAGES: Language[] = [
  { code: "en", name: "English" },
  { code: "fr", name: "French" },
  { code: "la", name: "Latin" },
  { code: "pt", name: "Portuguese" },
  { code: "es", name: "Spanish" }
];

interface Theme {
  code: string;
  name: string;
  description: string;
}

const THEMES: Theme[] = [
  { code: "business", name: "Business", description: "Strategy, corporate finance, governance & markets" },
  { code: "ecology", name: "Ecology", description: "Environment, sustainability & biomes" },
  { code: "law", name: "Law", description: "Jurisprudence, norms & legal procedures" },
  { code: "medicine", name: "Medicine", description: "Clinical diagnosis, healthcare & pharmacology" },
  { code: "mining", name: "Mining", description: "Geology, mineral processing & extraction" },
  { code: "politics", name: "Politics", description: "Governance, legislation & public policy" },
  { code: "technology", name: "Technology", description: "Software engineering, AI & cloud systems" }
];

export default function Home() {
  const [lang, setLang] = useState<string>("en");
  const [domainTheme, setDomainTheme] = useState<string>("business");
  const [type, setType] = useState<string>("paragraphs");
  const [count, setCount] = useState<number>(3);
  const [grammarCorrect, setGrammarCorrect] = useState<boolean>(true);
  const [orthographyCorrect, setOrthographyCorrect] = useState<boolean>(true);
  const [results, setResults] = useState<string[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [copied, setCopied] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [darkMode, setDarkMode] = useState<boolean>(false);
  const [showAbout, setShowAbout] = useState<boolean>(false);

  const isLatin = lang === "la";

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    if (savedTheme === "dark" || (!savedTheme && prefersDark)) {
      setDarkMode(true);
      document.documentElement.classList.add("dark");
      document.documentElement.classList.remove("light");
    } else {
      setDarkMode(false);
      document.documentElement.classList.add("light");
      document.documentElement.classList.remove("dark");
    }
  }, []);

  const toggleTheme = () => {
    if (darkMode) {
      setDarkMode(false);
      localStorage.setItem("theme", "light");
      document.documentElement.classList.add("light");
      document.documentElement.classList.remove("dark");
    } else {
      setDarkMode(true);
      localStorage.setItem("theme", "dark");
      document.documentElement.classList.add("dark");
      document.documentElement.classList.remove("light");
    }
  };

  const handleGenerate = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const apiBase = process.env.NEXT_PUBLIC_API_URL || "";
      const response = await fetch(`${apiBase}/api/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          lang,
          type,
          theme: isLatin ? "business" : domainTheme,
          count,
          grammar_correct: isLatin ? true : grammarCorrect,
          orthography_correct: isLatin ? true : orthographyCorrect
        })
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => null);
        const detail = errorData?.detail || `API error (${response.status})`;
        throw new Error(detail);
      }

      const data = await response.json();
      setResults(data.results);
    } catch (err: any) {
      console.error("API error:", err);
      setError(err?.message || "Failed to connect to API. Please ensure backend is running.");
    } finally {
      setLoading(false);
    }
  }, [lang, type, domainTheme, count, grammarCorrect, orthographyCorrect, isLatin]);

  useEffect(() => {
    handleGenerate();
  }, [handleGenerate]);

  const handleCopy = async () => {
    const textToCopy = results.join("\n\n");
    if (!textToCopy) return;

    try {
      await navigator.clipboard.writeText(textToCopy);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error("Failed to copy text: ", err);
    }
  };

  return (
    <div className="md:h-screen md:max-h-screen flex flex-col overflow-x-hidden md:overflow-hidden transition-colors duration-200">
      {/* Header */}
      <header className="shrink-0 border-b border-zinc-200 dark:border-zinc-800 bg-white/50 dark:bg-zinc-900/50 backdrop-blur-md sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="h-9 w-9 rounded-lg bg-brand text-white flex items-center justify-center shadow-md shadow-brand/20 border border-brand/30">
              <svg viewBox="6 -2 82 100" fill="currentColor" className="w-7 h-7 text-white">
                <g transform="matrix(0.24406519,-0.96975883,-0.96975883,-0.24406519,82.202474,108.06489)">
                  <path d="m26.754 80.539h-8.0117c-0.49609 0-0.96875-0.1875-1.332-0.52344 0 0-4.3906-4.0508-11.164-4.0508-1.0781 0-1.9531-0.875-1.9531-1.9531v-4.5742c0-1.0781 0.875-1.9531 1.9531-1.9531h20.508v-0.6875c0-1.0781 0.875-1.9531 1.9531-1.9531h8.7812c1.0781 0 1.9531 0.875 1.9531 1.9531v1.9883h22.137c6.3711-0.27344 12.062-1.9336 16.285-5.4727 4.5195-3.7891 7.1641-9.7266 7.3945-17.977 0.35156-12.637-11.305-18.285-19.93-18.137-7.5273 0.12891-13.871 4.9492-14.363 12.48-0.38672 5.9297 2.6055 10.184 7.0352 11.723 1.7266 0.60156 5.0469 0.42188 7.8008-0.60547 1.2227-0.45703 2.4453-1 2.8906-2.1328 0.60547-1.543 0.57422-3.3594-0.64453-4.2773-0.94922-0.71875-2.3789-0.67578-4.2109-0.16016-2.7656 0.77734-5.6406-0.83203-6.4219-3.5977-0.77734-2.7656 0.83203-5.6406 3.5977-6.4219 5.832-1.6445 10.266-0.41797 13.301 1.8672 4.7539 3.5859 6.4297 10.359 4.0664 16.387-1.4922 3.8047-4.832 6.5508-8.9375 8.0859-5.2305 1.957-11.582 1.8281-14.863 0.68359-8.5117-2.9609-14.742-10.84-14-22.227 0.85156-13.109 11.461-21.984 24.566-22.215 13.434-0.23437 31.059 9.1445 30.512 28.832-0.32812 11.871-4.6055 20.207-11.109 25.66-4.457 3.7383-10.039 6.1289-16.348 7.2344-2.7266 0.47656-5.5898 0.71094-8.5547 0.71094h-20.207v1.9883c0 1.0781-0.875 1.9531-1.9531 1.9531h-8.7812c-1.0781 0-1.9531-0.875-1.9531-1.9531v-0.6875zm0-9.1523h-18.555v0.76172c5.7109 0.53906 9.7656 3.3125 11.25 4.4844h7.3047zm3.9062 7.1992v0.6875h4.875v-10.523h-4.875zm8.7812-3.2539h20.207c2.7305 0 5.3711-0.21484 7.8828-0.65234 5.5938-0.97656 10.559-3.0664 14.512-6.3789 5.7578-4.8281 9.4258-12.266 9.7148-22.777 0.47266-17.039-14.914-25.02-26.543-24.82-11.012 0.19141-20.023 7.5469-20.738 18.562-0.60547 9.3398 4.4062 15.859 11.387 18.285 2.6992 0.9375 7.9102 0.95312 12.211-0.65625 3.0195-1.1289 5.5703-3.0508 6.668-5.8516 1.7031-4.3438 0.64453-9.2578-2.7812-11.844-2.25-1.6953-5.5625-2.4453-9.8906-1.2266-0.69141 0.19531-1.0938 0.91406-0.89844 1.6016 0.19531 0.69141 0.91406 1.0938 1.6016 0.89844 3.3281-0.9375 5.8906-0.50391 7.6211 0.80078 2.543 1.918 3.1914 5.5977 1.9258 8.8203-0.83594 2.1328-2.8555 3.5078-5.1602 4.3672-3.6797 1.375-8.1406 1.4375-10.449 0.63672-5.9609-2.0742-10.168-7.6875-9.6484-15.664 0.625-9.6211 8.5703-15.965 18.191-16.133 10.426-0.17969 24.324 6.8711 23.898 22.148-0.26562 9.6094-3.5234 16.445-8.7891 20.859-4.8477 4.0664-11.355 6.0742-18.672 6.3828h-0.082031-22.176v2.6406z" fillRule="evenodd" />
                </g>
                <rect fill="currentColor" width="5.639" height="2.256" x="22.473" y="29.788" />
                <rect fill="currentColor" width="5.639" height="2.256" x="35.274" y="-5.728" transform="rotate(27.284)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="6.537" y="-55.344" transform="rotate(88.533)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="-27.009" y="-69.811" transform="rotate(121.609)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="-67.571" y="-54.221" transform="rotate(162.95)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="-82.87" y="-35.328" transform="rotate(-169.331)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="-48.353" y="59.716" transform="rotate(-81.59)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="21.322" y="51.947" transform="rotate(-20.896)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="49.536" y="-15.931" transform="rotate(44.116)" />
                <rect fill="currentColor" width="5.639" height="2.256" x="-33.848" y="-61.633" transform="rotate(144.375)" />
              </svg>
            </div>
            <div>
              <h1 className="text-xl font-extrabold tracking-tight font-manrope text-zinc-900 dark:text-zinc-50">Prolixo</h1>
              <p className="text-[10px] text-zinc-500 dark:text-zinc-400">AI-powered natural language placeholder generator</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <Sun className={`w-4 h-4 transition-colors ${!darkMode ? "text-amber-500" : "text-zinc-400 dark:text-zinc-600"}`} />
            <button
              type="button"
              role="switch"
              aria-checked={darkMode}
              data-state={darkMode ? "checked" : "unchecked"}
              onClick={toggleTheme}
              className="relative inline-flex h-6 w-11 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-brand bg-zinc-200 dark:bg-zinc-700 radix-state-checked:bg-brand dark:radix-state-checked:bg-brand"
              title={darkMode ? "Switch to light mode" : "Switch to dark mode"}
              aria-label="Toggle dark mode"
            >
              <span
                data-state={darkMode ? "checked" : "unchecked"}
                className="pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white dark:bg-zinc-100 shadow-md ring-0 transition duration-200 ease-in-out radix-state-checked:translate-x-5 radix-state-unchecked:translate-x-0"
              />
            </button>
            <Moon className={`w-4 h-4 transition-colors ${darkMode ? "text-indigo-400" : "text-zinc-400 dark:text-zinc-600"}`} />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 min-h-0 max-w-6xl w-full mx-auto px-4 py-5 md:py-8 grid grid-cols-1 md:grid-cols-5 gap-6 md:gap-8 items-stretch overflow-hidden">

        {/* Settings Sidebar */}
        <section className="md:col-span-2 flex flex-col min-h-0 h-full">
          <div className="bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-5 md:p-6 shadow-sm flex flex-col justify-between h-full min-h-0 gap-8 md:gap-10 overflow-y-auto">

            <div className="flex flex-col gap-7 md:gap-9">
              {/* Language Selector */}
              <div className="flex flex-col gap-3">
                <label className="text-sm font-semibold text-zinc-700 dark:text-zinc-300 flex items-center gap-2">
                  <Languages className="w-4 h-4 text-zinc-500" />
                  Language
                </label>

                <Select.Root value={lang} onValueChange={setLang}>
                  <Select.Trigger
                    className="w-full flex items-center justify-between px-4 py-3 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-950 text-sm font-medium hover:bg-zinc-100 dark:hover:bg-zinc-900 focus:outline-none focus:ring-2 focus:ring-brand transition-all text-zinc-900 dark:text-zinc-100"
                    aria-label="Language"
                  >
                    <Select.Value />
                    <Select.Icon>
                      <ChevronDown className="w-4 h-4 text-zinc-500" />
                    </Select.Icon>
                  </Select.Trigger>

                  <Select.Portal>
                    <Select.Content
                      position="popper"
                      side="bottom"
                      sideOffset={4}
                      avoidCollisions={false}
                      className="overflow-hidden bg-white dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800 shadow-xl z-50 w-[var(--radix-select-trigger-width)]"
                    >
                      <Select.ScrollUpButton className="flex items-center justify-center h-6 bg-white dark:bg-zinc-900 text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-200 cursor-default">
                        <ChevronUp className="w-4 h-4" />
                      </Select.ScrollUpButton>
                      <Select.Viewport className="p-1 max-h-[220px] overflow-y-auto">
                        {LANGUAGES.map((item) => (
                          <Select.Item
                            key={item.code}
                            value={item.code}
                            className="flex items-center px-4 py-2.5 rounded-lg text-sm font-medium cursor-pointer select-none outline-none text-zinc-900 dark:text-zinc-100 hover:bg-zinc-100 dark:hover:bg-zinc-800 data-[state=checked]:bg-brand data-[state=checked]:text-white dark:data-[state=checked]:bg-brand dark:data-[state=checked]:text-white transition-colors"
                          >
                            <Select.ItemText>{item.name}</Select.ItemText>
                          </Select.Item>
                        ))}
                      </Select.Viewport>
                      <Select.ScrollDownButton className="flex items-center justify-center h-6 bg-white dark:bg-zinc-900 text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-200 cursor-default">
                        <ChevronDown className="w-4 h-4" />
                      </Select.ScrollDownButton>
                    </Select.Content>
                  </Select.Portal>
                </Select.Root>
              </div>

              {/* Theme Selector */}
              <div className="flex flex-col gap-3">
                <label className="text-sm font-semibold text-zinc-700 dark:text-zinc-300 flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-zinc-500" />
                  Theme
                </label>

                {isLatin ? (
                  <div
                    className="w-full flex items-center justify-between px-4 py-3 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-100/70 dark:bg-zinc-900/50 text-sm font-medium text-zinc-400 dark:text-zinc-500 cursor-not-allowed select-none"
                    title="Theme selection is not available for Latin"
                  >
                    <span>-</span>
                    <ChevronDown className="w-4 h-4 text-zinc-400 dark:text-zinc-600" />
                  </div>
                ) : (
                  <Select.Root value={domainTheme} onValueChange={setDomainTheme}>
                    <Select.Trigger
                      className="w-full flex items-center justify-between px-4 py-3 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-950 text-sm font-medium hover:bg-zinc-100 dark:hover:bg-zinc-900 focus:outline-none focus:ring-2 focus:ring-brand transition-all text-zinc-900 dark:text-zinc-100 cursor-pointer"
                      aria-label="Theme"
                    >
                      <Select.Value />
                      <Select.Icon>
                        <ChevronDown className="w-4 h-4 text-zinc-500" />
                      </Select.Icon>
                    </Select.Trigger>

                    <Select.Portal>
                      <Select.Content
                        position="popper"
                        side="bottom"
                        sideOffset={4}
                        avoidCollisions={false}
                        className="overflow-hidden bg-white dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800 shadow-xl z-50 w-[var(--radix-select-trigger-width)]"
                      >
                        <Select.ScrollUpButton className="flex items-center justify-center h-6 bg-white dark:bg-zinc-900 text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-200 cursor-default">
                          <ChevronUp className="w-4 h-4" />
                        </Select.ScrollUpButton>
                        <Select.Viewport className="p-1 max-h-[220px] overflow-y-auto">
                          {THEMES.map((item) => (
                            <Select.Item
                              key={item.code}
                              value={item.code}
                              className="group flex flex-col px-4 py-2.5 rounded-lg text-sm cursor-pointer select-none outline-none text-zinc-900 dark:text-zinc-100 hover:bg-zinc-100 dark:hover:bg-zinc-800 data-[state=checked]:bg-brand data-[state=checked]:text-white dark:data-[state=checked]:bg-brand dark:data-[state=checked]:text-white transition-colors"
                            >
                              <Select.ItemText className="font-semibold text-zinc-900 dark:text-zinc-100 group-data-[state=checked]:text-white dark:group-data-[state=checked]:text-white">
                                {item.name}
                              </Select.ItemText>
                              <span className="text-xs text-zinc-500 dark:text-zinc-400 group-data-[state=checked]:text-white/90 dark:group-data-[state=checked]:text-white/90">
                                {item.description}
                              </span>
                            </Select.Item>
                          ))}
                        </Select.Viewport>
                        <Select.ScrollDownButton className="flex items-center justify-center h-6 bg-white dark:bg-zinc-900 text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-200 cursor-default">
                          <ChevronDown className="w-4 h-4" />
                        </Select.ScrollDownButton>
                      </Select.Content>
                    </Select.Portal>
                  </Select.Root>
                )}
              </div>

              {/* Linguistic Precision / Correctness Switches */}
              <div className="flex flex-col gap-3">
                <div className="flex items-center gap-1.5">
                  <label className="text-sm font-semibold text-zinc-700 dark:text-zinc-300 flex items-center gap-2">
                    <SpellCheck className="w-4 h-4 text-zinc-500" />
                    Linguistic Precision
                  </label>

                  <div className="relative flex items-center group">
                    <button
                      type="button"
                      className="text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-200 transition-colors focus:outline-none cursor-help"
                      aria-label="About Linguistic Precision"
                    >
                      <Info className="w-3.5 h-3.5" />
                    </button>
                    <div className="absolute left-1/2 -translate-x-1/2 bottom-full mb-2 hidden group-hover:flex group-focus-within:flex flex-col w-60 p-3 bg-zinc-900 dark:bg-zinc-800 text-white text-xs leading-relaxed rounded-xl shadow-xl border border-zinc-700/50 z-50 pointer-events-none transition-all animate-fadeIn">
                      <span className="font-semibold text-zinc-100 mb-1">Linguistic Precision</span>
                      <span className="text-zinc-300 dark:text-zinc-300 text-[11px]">
                        Controls whether text is generated error-free or with realistic grammatical and orthographical noise to test spellcheckers and NLP correction models.
                      </span>
                      <div className="absolute left-1/2 -translate-x-1/2 top-full -mt-1 border-4 border-transparent border-t-zinc-900 dark:border-t-zinc-800" />
                    </div>
                  </div>
                </div>

                <div className="flex flex-col gap-2.5">
                  {/* Grammar Switch */}
                  <div
                    className={`flex items-center justify-between px-3.5 py-2.5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-950 transition-opacity ${
                      isLatin ? "opacity-50 cursor-not-allowed" : ""
                    }`}
                    title={isLatin ? "Not applicable for Latin (Lorem Ipsum)" : undefined}
                  >
                    <span className="text-xs font-semibold text-zinc-800 dark:text-zinc-200">Grammar</span>
                    <div className="flex items-center gap-1.5">
                      <ThumbsDown
                        className={`w-3.5 h-3.5 transition-colors ${
                          !grammarCorrect && !isLatin ? "text-amber-500" : "text-zinc-300 dark:text-zinc-600"
                        }`}
                      />
                      <button
                        type="button"
                        role="switch"
                        disabled={isLatin}
                        aria-checked={grammarCorrect}
                        onClick={() => setGrammarCorrect(!grammarCorrect)}
                        className={`relative inline-flex h-5 w-9 shrink-0 rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-brand ${
                          isLatin
                            ? "cursor-not-allowed bg-zinc-300 dark:bg-zinc-800"
                            : grammarCorrect
                            ? "bg-brand cursor-pointer"
                            : "bg-zinc-300 dark:bg-zinc-700 cursor-pointer"
                        }`}
                        title={
                          isLatin
                            ? "Not applicable for Latin"
                            : grammarCorrect
                            ? "Grammar: Correct (no duplicate/syntax errors)"
                            : "Grammar: Injected errors enabled"
                        }
                        aria-label="Toggle grammar correctness"
                      >
                        <span
                          className={`pointer-events-none inline-block h-4 w-4 transform rounded-full bg-white dark:bg-zinc-100 shadow-md ring-0 transition duration-200 ease-in-out ${
                            grammarCorrect ? "translate-x-4" : "translate-x-0"
                          }`}
                        />
                      </button>
                      <ThumbsUp
                        className={`w-3.5 h-3.5 transition-colors ${
                          grammarCorrect && !isLatin ? "text-brand" : "text-zinc-300 dark:text-zinc-600"
                        }`}
                      />
                    </div>
                  </div>

                  {/* Orthography Switch */}
                  <div
                    className={`flex items-center justify-between px-3.5 py-2.5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-950 transition-opacity ${
                      isLatin ? "opacity-50 cursor-not-allowed" : ""
                    }`}
                    title={isLatin ? "Not applicable for Latin (Lorem Ipsum)" : undefined}
                  >
                    <span className="text-xs font-semibold text-zinc-800 dark:text-zinc-200">Orthography</span>
                    <div className="flex items-center gap-1.5">
                      <ThumbsDown
                        className={`w-3.5 h-3.5 transition-colors ${
                          !orthographyCorrect && !isLatin ? "text-amber-500" : "text-zinc-300 dark:text-zinc-600"
                        }`}
                      />
                      <button
                        type="button"
                        role="switch"
                        disabled={isLatin}
                        aria-checked={orthographyCorrect}
                        onClick={() => setOrthographyCorrect(!orthographyCorrect)}
                        className={`relative inline-flex h-5 w-9 shrink-0 rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-brand ${
                          isLatin
                            ? "cursor-not-allowed bg-zinc-300 dark:bg-zinc-800"
                            : orthographyCorrect
                            ? "bg-brand cursor-pointer"
                            : "bg-zinc-300 dark:bg-zinc-700 cursor-pointer"
                        }`}
                        title={
                          isLatin
                            ? "Not applicable for Latin"
                            : orthographyCorrect
                            ? "Orthography: Correct"
                            : "Orthography: Injected spelling errors"
                        }
                        aria-label="Toggle orthography correctness"
                      >
                        <span
                          className={`pointer-events-none inline-block h-4 w-4 transform rounded-full bg-white dark:bg-zinc-100 shadow-md ring-0 transition duration-200 ease-in-out ${
                            orthographyCorrect ? "translate-x-4" : "translate-x-0"
                          }`}
                        />
                      </button>
                      <ThumbsUp
                        className={`w-3.5 h-3.5 transition-colors ${
                          orthographyCorrect && !isLatin ? "text-brand" : "text-zinc-300 dark:text-zinc-600"
                        }`}
                      />
                    </div>
                  </div>
                </div>
              </div>

              {/* Output Format (Words, Sentences or Paragraphs) */}
              <div className="flex flex-col gap-3">
                <label className="text-sm font-semibold text-zinc-700 dark:text-zinc-300 flex items-center gap-2">
                  <FileText className="w-4 h-4 text-zinc-500" />
                  Format
                </label>

                <Tabs.Root
                  value={type}
                  onValueChange={(val) => {
                    setType(val);
                    if (val === "words") {
                      if (count > 100) setCount(100);
                      else if (count < 5) setCount(20);
                    } else if (val === "sentences") {
                      if (count > 25) setCount(25);
                    } else if (val === "paragraphs") {
                      if (count > 10) setCount(10);
                    }
                  }}
                  className="w-full"
                >
                  <Tabs.List className="flex bg-zinc-100 dark:bg-zinc-950 p-1 rounded-xl gap-1 border border-zinc-200 dark:border-zinc-900">
                    <Tabs.Trigger
                      value="words"
                      className="flex-1 flex items-center justify-center gap-1.5 px-2.5 py-2 rounded-lg text-xs font-semibold select-none outline-none cursor-pointer text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200/70 dark:hover:bg-zinc-800/70 hover:text-zinc-900 dark:hover:text-zinc-100 radix-state-active:bg-brand radix-state-active:text-white dark:radix-state-active:bg-brand dark:radix-state-active:text-white radix-state-active:shadow-sm radix-state-active:hover:bg-brand transition-all"
                    >
                      <Type className="w-3.5 h-3.5" />
                      Words
                    </Tabs.Trigger>
                    <Tabs.Trigger
                      value="sentences"
                      className="flex-1 flex items-center justify-center gap-1.5 px-2.5 py-2 rounded-lg text-xs font-semibold select-none outline-none cursor-pointer text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200/70 dark:hover:bg-zinc-800/70 hover:text-zinc-900 dark:hover:text-zinc-100 radix-state-active:bg-brand radix-state-active:text-white dark:radix-state-active:bg-brand dark:radix-state-active:text-white radix-state-active:shadow-sm radix-state-active:hover:bg-brand transition-all"
                    >
                      <AlignLeft className="w-3.5 h-3.5" />
                      Sentences
                    </Tabs.Trigger>
                    <Tabs.Trigger
                      value="paragraphs"
                      className="flex-1 flex items-center justify-center gap-1.5 px-2.5 py-2 rounded-lg text-xs font-semibold select-none outline-none cursor-pointer text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200/70 dark:hover:bg-zinc-800/70 hover:text-zinc-900 dark:hover:text-zinc-100 radix-state-active:bg-brand radix-state-active:text-white dark:radix-state-active:bg-brand dark:radix-state-active:text-white radix-state-active:shadow-sm radix-state-active:hover:bg-brand transition-all"
                    >
                      <FileText className="w-3.5 h-3.5" />
                      Paragraphs
                    </Tabs.Trigger>
                  </Tabs.List>
                </Tabs.Root>
              </div>

              {/* Quantity Slider */}
              <div className="flex flex-col gap-4">
                <div className="flex justify-between items-center">
                  <label className="text-sm font-semibold text-zinc-700 dark:text-zinc-300">
                    Amount
                  </label>
                  <span className="text-sm font-bold bg-zinc-100 dark:bg-zinc-800 text-zinc-900 dark:text-zinc-100 px-2 py-0.5 rounded-md min-w-8 text-center border border-zinc-200 dark:border-zinc-700">
                    {count}
                  </span>
                </div>

                <Slider.Root
                  value={[count]}
                  onValueChange={(val) => setCount(val[0])}
                  max={type === "words" ? 100 : type === "sentences" ? 25 : 10}
                  min={type === "words" ? 5 : 1}
                  step={1}
                  className="relative flex items-center select-none touch-none w-full h-5 cursor-pointer"
                >
                  <Slider.Track className="bg-zinc-200 dark:bg-zinc-800 relative grow rounded-full h-[6px]">
                    <Slider.Range className="absolute bg-brand rounded-full h-full" />
                  </Slider.Track>
                  <Slider.Thumb className="block w-5 h-5 bg-white border-2 border-brand rounded-full hover:scale-110 active:scale-95 focus:outline-none focus:ring-2 focus:ring-brand/40 transition-all shadow-sm" />
                </Slider.Root>

                <span className="text-[10px] text-zinc-400 dark:text-zinc-500">
                  {type === "words" ? "Max 100 words per generation." : type === "sentences" ? "Max 25 sentences per generation." : "Max 10 paragraphs per generation."}
                </span>
              </div>
            </div>

            {/* Generate Button */}
            <button
              onClick={handleGenerate}
              disabled={loading}
              className="w-full flex items-center justify-center gap-2 py-3 px-4 bg-brand hover:bg-brand-hover active:bg-brand-active text-white rounded-xl font-semibold text-sm shadow-md hover:shadow-lg shadow-brand/20 disabled:opacity-50 disabled:cursor-not-allowed transition-all mt-auto"
            >
              {loading ? (
                <RefreshCw className="w-4 h-4 animate-spin" />
              ) : (
                <RefreshCw className="w-4 h-4" />
              )}
              Generate Placeholder
            </button>
          </div>
        </section>

        {/* Results Viewer */}
        <section className="md:col-span-3 flex flex-col min-h-0 h-full">
          <div className="bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-5 md:p-6 shadow-sm flex flex-col h-full min-h-0">

            {/* Results Header */}
            <div className="flex justify-between items-center border-b border-zinc-100 dark:border-zinc-800 pb-4 mb-4 shrink-0">
              <h2 className="text-sm font-semibold text-zinc-500 dark:text-zinc-400 tracking-wider uppercase">
                Generated Text ({type === "words" ? "Words" : type === "sentences" ? "Sentences" : "Paragraphs"})
              </h2>
              {results.length > 0 && (
                <button
                  onClick={handleCopy}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-zinc-200 dark:border-zinc-800 hover:border-brand/40 hover:bg-brand/5 hover:text-brand text-xs font-semibold text-zinc-700 dark:text-zinc-300 transition-colors focus:outline-none"
                  title="Copy to clipboard"
                >
                  {copied ? (
                    <>
                      <Check className="w-3.5 h-3.5 text-green-500" />
                      Copied!
                    </>
                  ) : (
                    <>
                      <Copy className="w-3.5 h-3.5" />
                      Copy
                    </>
                  )}
                </button>
              )}
            </div>

            {/* Results Body */}
            <div className="flex-1 min-h-0 overflow-y-auto pr-2 text-zinc-800 dark:text-zinc-200 text-sm leading-relaxed space-y-4 select-text">
              {results.length > 0 ? (
                results.map((item, index) => (
                  <p key={index} className="transition-all duration-300 animate-fadeIn">
                    {item}
                  </p>
                ))
              ) : (
                <div className="flex flex-col items-center justify-center text-center my-auto py-12 text-zinc-400 dark:text-zinc-600 gap-2 h-full">
                  <FileText className="w-12 h-12 stroke-[1.2]" />
                  <p className="text-sm font-medium">No text generated yet.</p>
                  <p className="text-xs">Adjust the settings and click Generate above.</p>
                </div>
              )}
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="shrink-0 border-t border-zinc-200 dark:border-zinc-800 py-3.5 bg-zinc-50 dark:bg-zinc-950/20">
        <div className="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between text-xs text-zinc-500 dark:text-zinc-500 gap-4">
          <p>© 2026 Prolixo. AI-powered statistical placeholder text generator for development and UI/UX design.</p>
          <div className="flex gap-4 items-center">
            <button
              onClick={() => setShowAbout(true)}
              className="flex items-center gap-1.5 text-brand dark:text-brand-light font-semibold hover:underline cursor-pointer transition-colors"
            >
              <Info className="w-3.5 h-3.5" />
              About & Inspirations
            </button>
            <span className="text-zinc-300 dark:text-zinc-700">•</span>
            <a
              href="https://github.com/rdornas/prolixo"
              target="_blank"
              rel="noreferrer"
              className="flex items-center gap-1.5 text-brand dark:text-brand-light font-semibold hover:underline cursor-pointer transition-colors"
              title="View source code on GitHub"
            >
              <Github className="w-4 h-4" />
              <span>GitHub</span>
            </a>
          </div>
        </div>
      </footer>

      {/* Centered Modal Overlay for About & Inspirations */}
      {showAbout && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fadeIn"
          onClick={(e) => {
            if (e.target === e.currentTarget) setShowAbout(false);
          }}
        >
          <div
            className="relative w-full max-w-2xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-2xl shadow-2xl p-6 md:p-8 max-h-[90vh] overflow-y-auto"
            role="dialog"
            aria-modal="true"
            aria-labelledby="about-title"
          >
            <button
              onClick={() => setShowAbout(false)}
              className="absolute top-4 right-4 p-2 text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-100 rounded-lg hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
              title="Close"
              aria-label="Close modal"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center gap-3 mb-6">
              <div className="h-10 w-10 rounded-xl bg-brand/10 text-brand flex items-center justify-center">
                <Info className="w-6 h-6" />
              </div>
              <div>
                <h3 id="about-title" className="text-xl font-bold text-zinc-900 dark:text-zinc-100">
                  About Prolixo & Inspirations
                </h3>
                <p className="text-xs text-zinc-500 dark:text-zinc-400">
                  Technical Foundations, Historical Sources & Credits
                </p>
              </div>
            </div>

            <div className="space-y-6 text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">
              <div>
                <h4 className="font-bold text-zinc-900 dark:text-zinc-100 text-base mb-1 flex items-center gap-2">
                  🎯 Project Purpose
                </h4>
                <p className="text-xs text-zinc-600 dark:text-zinc-400">
                  <strong>Prolixo</strong> is a statistical AI-powered natural language generation engine built for UI/UX designers and developers. It produces structured, highly-variable, and realistic text blocks in English, French, Portuguese, Spanish, and classical Latin.
                </p>
              </div>

              <div>
                <h4 className="font-bold text-zinc-900 dark:text-zinc-100 text-base mb-2 flex items-center gap-2">
                  💡 Key Inspirations & References
                </h4>
                <ul className="space-y-3 text-xs text-zinc-600 dark:text-zinc-400 leading-relaxed">
                  <li>
                    <strong className="text-zinc-900 dark:text-zinc-100 font-semibold">1. Gerador de Lero-Lero (Brazil):</strong>{" "}
                    The classic Brazilian corporate jargon generator that pioneered the concept of combining formal-sounding prose fragments to generate eloquent, non-committal text blocks.
                  </li>
                  <li>
                    <strong className="text-zinc-900 dark:text-zinc-100 font-semibold">2. Corporate Bullshit Generators:</strong>{" "}
                    Inspired by early corporate buzzword engines (such as the classic Ada Corporate Bullshit Generator), adapted into a modernized, non-repetitive formal placeholder system.
                  </li>
                  <li>
                    <strong className="text-zinc-900 dark:text-zinc-100 font-semibold">3. Postmodernism Generator:</strong>{" "}
                    Created by Andrew C. Bulhak in 1996, which popularized the creation of domain-specific, grammatically convincing text generators.
                  </li>
                </ul>
              </div>

              <div>
                <h4 className="font-bold text-zinc-900 dark:text-zinc-100 text-base mb-1 flex items-center gap-2">
                  🎨 Logo Design Credits
                </h4>
                <p className="text-xs text-zinc-500 dark:text-zinc-400">
                  The brand logo mark is derived from the icon created by <strong>Muhammad Nur Auliady Pamungkas</strong> from the{" "}
                  <a
                    href="https://thenounproject.com/icon/party-blower-8206017/"
                    target="_blank"
                    rel="noreferrer"
                    className="text-brand dark:text-brand-light hover:underline font-semibold"
                  >
                    Noun Project
                  </a>{" "}
                  (licensed under CC BY 3.0).
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
