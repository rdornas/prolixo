FROM golang:1.22-alpine AS builder

WORKDIR /app

COPY go.mod ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /prolixo-api ./cmd/server

FROM alpine:3.20

WORKDIR /app
COPY --from=builder /prolixo-api /app/prolixo-api

EXPOSE 8000

CMD ["/app/prolixo-api"]
