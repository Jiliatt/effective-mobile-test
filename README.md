# Effective Mobile — тестовое задание

## Технологии

- Python 3.12 — HTTP-сервер (backend)
- Nginx 1.27 — reverse proxy
- Docker / Docker Compose — контейнеризация

## Архитектура

```text
Клиент → Nginx (порт 80) → Backend (порт 8080) → "Hello from Effective Mobile!"
```

- **backend** — Python HTTP-сервер, слушает порт 8080, доступен только внутри Docker-сети
- **nginx** — reverse proxy, принимает запросы на порт 80 и проксирует на backend
- Сервисы общаются через выделенную Docker-сеть `app-network`
- Наружу опубликован только nginx (порт 80)

## Запуск

```bash
docker compose up -d --build
```

## Проверка

```bash
curl http://localhost
```

Ожидаемый ответ: `Hello from Effective Mobile!`

Проверка healthcheck:

```bash
docker inspect --format='{{.State.Health.Status}}' em-backend
```

## Остановка

```bash
docker compose down
```
