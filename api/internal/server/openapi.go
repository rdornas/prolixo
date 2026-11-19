package server

const openAPISpec = `{
  "openapi": "3.0.3",
  "info": {
    "title": "Prolixo API",
    "version": "1.0.0",
    "description": "Multilingual thematic placeholder text generator API."
  },
  "paths": {
    "/": {
      "get": {
        "summary": "Health Check",
        "responses": {
          "200": {
            "description": "API online status"
          }
        }
      }
    },
    "/api/languages": {
      "get": {
        "summary": "List Supported Languages",
        "responses": {
          "200": {
            "description": "List of supported languages"
          }
        }
      }
    },
    "/api/themes": {
      "get": {
        "summary": "List Supported Themes",
        "responses": {
          "200": {
            "description": "List of supported domain themes"
          }
        }
      }
    },
    "/api/generate": {
      "post": {
        "summary": "Generate Placeholder Text",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GenerateRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Generated text results",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GenerateResponse"
                }
              }
            }
          },
          "400": { "description": "Unsupported language or output type" },
          "422": { "description": "Validation error" },
          "429": { "description": "Rate limit exceeded" }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "GenerateRequest": {
        "type": "object",
        "required": ["lang", "type", "count"],
        "properties": {
          "lang": { "type": "string", "enum": ["en", "fr", "la", "pt", "es"] },
          "type": { "type": "string", "enum": ["words", "sentences", "paragraphs"] },
          "theme": { "type": "string", "default": "business" },
          "count": { "type": "integer", "minimum": 1, "maximum": 100 },
          "grammar_correct": { "type": "boolean", "default": true },
          "orthography_correct": { "type": "boolean", "default": true }
        }
      },
      "GenerateResponse": {
        "type": "object",
        "properties": {
          "lang": { "type": "string" },
          "type": { "type": "string" },
          "theme": { "type": "string" },
          "count": { "type": "integer" },
          "grammar_correct": { "type": "boolean" },
          "orthography_correct": { "type": "boolean" },
          "results": { "type": "array", "items": { "type": "string" } }
        }
      }
    }
  }
}`

const swaggerHTML = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Prolixo API - Swagger UI</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css" />
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    window.onload = () => {
      SwaggerUIBundle({
        url: '/api/openapi.json',
        dom_id: '#swagger-ui'
      });
    };
  </script>
</body>
</html>`
