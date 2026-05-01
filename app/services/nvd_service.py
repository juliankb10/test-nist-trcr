import httpx

from fastapi import HTTPException

BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"


async def fetch_vulnerabilities(
    params: dict | None = None,
):

    try:

        async with httpx.AsyncClient(
            timeout=30
        ) as client:

            response = await client.get(
                BASE_URL,
                params=params,
            )

            response.raise_for_status()

            return response.json()

    except httpx.HTTPError:

        raise HTTPException(
            status_code=503,
            detail="NVD service unavailable",
        )