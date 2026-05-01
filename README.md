# CVE Manager API

API REST desarrollada con FastAPI para consultar vulnerabilidades del NVD (NIST) y gestionar vulnerabilidades corregidas.

## Tecnologías

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Ejecución

````bash
docker compose up --build

---

## 5. Swagger

```md id="jlwm1o"
## Swagger

http://localhost:8000/docs

## Endpoints

### GET /v1/vulnerabilities

Obtiene listado de vulnerabilidades.

### POST /v1/fixed

Marca vulnerabilidades como corregidas.

### GET /v1/vulnerabilities/active

Obtiene vulnerabilidades activas.

### GET /v1/vulnerabilities/summary

Obtiene resumen por severidad.

## Variables de entorno

DATABASE_URL=postgresql://postgres:postgres@db:5432/vulnerabilities

## Ejemplos

### Obtener vulnerabilidades

```bash
curl http://localhost:8000/v1/vulnerabilities
````

### Marcar como fixed

curl -X POST http://localhost:8000/v1/fixed \
-H "Content-Type: application/json" \
-d '{
"cve_ids": ["CVE-2024-1234"]
}'
