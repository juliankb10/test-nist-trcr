from fastapi import FastAPI

from app.core.database import (
    Base,
    engine,
)

from app.models.fixed_vulnerability import (
    FixedVulnerability,
)

from fastapi.middleware.cors import (
    CORSMiddleware,
)

from fastapi.staticfiles import (
    StaticFiles,
)

from app.api.v1.router import api_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CVE Manager API",
)

app.include_router(api_router)