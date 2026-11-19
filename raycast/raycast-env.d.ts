/// <reference types="@raycast/api">

/* 🚧 🚧 🚧
 * This file is auto-generated from the extension's manifest.
 * Do not modify manually. Instead, update the `package.json` file.
 * 🚧 🚧 🚧 */

/* eslint-disable @typescript-eslint/ban-types */

type ExtensionPreferences = {
  /** Language - Language used by quick Generate Paragraphs/Sentences/Words commands. */
  "defaultLang": "pt" | "en" | "es" | "fr" | "la",
  /** Theme - Domain theme used by quick commands (ignored for Latin). */
  "defaultTheme": "business" | "ecology" | "law" | "medicine" | "mining" | "politics" | "technology",
  /** Grammar Correct - Whether quick commands should generate grammatically correct text. */
  "grammarCorrect": boolean,
  /** Orthography Correct - Whether quick commands should generate orthographically correct text. */
  "orthographyCorrect": boolean,
  /** Quick Command Action - Action performed after Generate Paragraphs/Sentences/Words finishes. */
  "quickAction": "copy" | "paste",
  /** API Base URL - Base URL of the Prolixo API (defaults to the online production API). */
  "apiUrl": string
}

/** Preferences accessible in all the extension's commands */
declare type Preferences = ExtensionPreferences

declare namespace Preferences {
  /** Preferences accessible in the `generate-paragraphs` command */
  export type GenerateParagraphs = ExtensionPreferences & {}
  /** Preferences accessible in the `generate-sentences` command */
  export type GenerateSentences = ExtensionPreferences & {}
  /** Preferences accessible in the `generate-words` command */
  export type GenerateWords = ExtensionPreferences & {}
  /** Preferences accessible in the `generate-text` command */
  export type GenerateText = ExtensionPreferences & {}
}

declare namespace Arguments {
  /** Arguments passed to the `generate-paragraphs` command */
  export type GenerateParagraphs = {
  /** No. of Paragraphs */
  "count": string
}
  /** Arguments passed to the `generate-sentences` command */
  export type GenerateSentences = {
  /** No. of Sentences */
  "count": string
}
  /** Arguments passed to the `generate-words` command */
  export type GenerateWords = {
  /** No. of Words */
  "count": string
}
  /** Arguments passed to the `generate-text` command */
  export type GenerateText = {}
}

