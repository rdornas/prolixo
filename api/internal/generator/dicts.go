package generator

import (
	"embed"
	"encoding/json"
	"fmt"
)

//go:embed data/*.json
var dictFS embed.FS

type romanceDict map[string][]string
type englishDict map[string][]string
type latinDict struct {
	Sentences []string `json:"sentences"`
}

// themeEntry holds either a categorized lexicon map or a flat word list (used for Latin).
type themeEntry struct {
	Map  map[string][]string
	List []string
}

func (t *themeEntry) UnmarshalJSON(data []byte) error {
	if len(data) > 0 && data[0] == '[' {
		return json.Unmarshal(data, &t.List)
	}
	return json.Unmarshal(data, &t.Map)
}

// themeDicts maps lang -> theme -> themeEntry
type themeDicts map[string]map[string]themeEntry

var (
	ptDict     romanceDict
	esDict     romanceDict
	frDict     romanceDict
	enDict     englishDict
	laDict     latinDict
	themesData themeDicts
)

func init() {
	if err := loadJSON("data/pt.json", &ptDict); err != nil {
		panic(fmt.Sprintf("failed to load pt.json: %v", err))
	}
	if err := loadJSON("data/es.json", &esDict); err != nil {
		panic(fmt.Sprintf("failed to load es.json: %v", err))
	}
	if err := loadJSON("data/fr.json", &frDict); err != nil {
		panic(fmt.Sprintf("failed to load fr.json: %v", err))
	}
	if err := loadJSON("data/en.json", &enDict); err != nil {
		panic(fmt.Sprintf("failed to load en.json: %v", err))
	}
	if err := loadJSON("data/la.json", &laDict); err != nil {
		panic(fmt.Sprintf("failed to load la.json: %v", err))
	}
	if err := loadJSON("data/themes.json", &themesData); err != nil {
		panic(fmt.Sprintf("failed to load themes.json: %v", err))
	}
}

func loadJSON(path string, target any) error {
	raw, err := dictFS.ReadFile(path)
	if err != nil {
		return err
	}
	return json.Unmarshal(raw, target)
}
