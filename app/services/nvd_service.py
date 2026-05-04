import httpx

from app.core.config import settings
from fastapi import HTTPException

async def fetch_vulnerabilities(
    params: dict | None = None,
):

    try:

        async with httpx.AsyncClient(
            timeout=30
        ) as client:

            response = await client.get(
                settings.nvd_api,
                params=params,
            )

            response.raise_for_status()

            return response.json()

    except httpx.HTTPError:

        raise HTTPException(
            status_code=503,
            detail="NVD service unavailable",
        )