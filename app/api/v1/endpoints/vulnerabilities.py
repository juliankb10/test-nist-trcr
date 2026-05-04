from fastapi import APIRouter, Depends
from fastapi import APIRouter, Query
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

from app.schemas.vulnerability import (
    VulnerabilityListResponse,
)

from app.services.nvd_service import (
    fetch_vulnerabilities,
)

from app.services.vulnerability_service import (
    extract_severity,
)

from app.repositories.fixed_repository import (
    FixedRepository,
)

from app.api.dependencies import (
    get_current_user,
)

router = APIRouter()

@router.get(
    "/vulnerabilities",
    response_model=VulnerabilityListResponse,
)
async def get_vulnerabilities(
    current_user: str = Depends(
        get_current_user
    ),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    severity: str | None = Query(
        default=None
    ),
):

    start_index = (page - 1) * page_size
    params = {
        "startIndex": start_index,
        "resultsPerPage": page_size,
    }

    data = await fetch_vulnerabilities(params)
    items = []

    for item in data.get("vulnerabilities", []):
        cve = item.get("cve", {})
        current_severity = extract_severity(item)
        if severity and severity != current_severity:
            continue

        items.append({
            "cve_id": cve.get("id"),
            "severity": current_severity,
            "description": cve.get(
                "descriptions",
                [{}]
            )[0].get("value"),
        })

    return {
        "page": page,
        "page_size": page_size,
        "total": data.get("totalResults"),
        "items": items,
    }


@router.get("/vulnerabilities/active")
async def get_active_vulnerabilities(
    current_user: str = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db),
):

    data = await fetch_vulnerabilities()
    fixed_ids = FixedRepository.get_all_fixed_ids(
        db
    )
    active = []

    for item in data.get("vulnerabilities", []):
        cve = item.get("cve", {})
        cve_id = cve.get("id")
        if cve_id in fixed_ids:
            continue

        active.append({
            "cve_id": cve_id,
            "severity": extract_severity(item),
        })

    return active

@router.get("/vulnerabilities/summary")
async def get_summary(
    current_user: str = Depends(
        get_current_user
    ),):

    data = await fetch_vulnerabilities()
    summary = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
    }

    for item in data.get("vulnerabilities", []):
        severity = extract_severity(item)
        if severity in summary:
            summary[severity] += 1

    return summary