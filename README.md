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
JWT_SECRET_KEY=Julian*123
NVD_API=https://services.nvd.nist.gov/rest/json/cves/2.0

## Ejemplos

### Obtener vulnerabilidades

```bash
curl http://localhost:8000/v1/vulnerabilities

### Marcar como fixed

```bash
curl -X POST http://localhost:8000/v1/fixed \
-H "Content-Type: application/json" \
-d '{
"cve_ids": ["CVE-2024-1234"]
}'
````
