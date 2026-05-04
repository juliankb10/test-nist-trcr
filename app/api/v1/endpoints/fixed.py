from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

from app.schemas.fixed import (
    FixedVulnerabilityRequest,
)

from app.repositories.fixed_repository import (
    FixedRepository,
)

from app.api.dependencies import (
    get_current_user,
)

router = APIRouter()

@router.post("/fixed")
async def mark_fixed(
    payload: FixedVulnerabilityRequest,
    current_user: str = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db),
):

    for cve_id in payload.cve_ids:
        exists = FixedRepository.exists(
            db,
            cve_id,
        )

        if exists:
            return {
                "message": "The vulnerability has already been marked"
            }

        if not exists:
            FixedRepository.create(
                db,
                cve_id,
            )

    FixedRepository.save(db)

    return {
        "message": "Vulnerabilities marked as fixed"
    }

@router.delete("/fixed/{cve_id}")
async def unmark_fixed(
    cve_id: str,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    
    exists = FixedRepository.exists(
        db,
        cve_id,
    )

    if not exists:
        raise HTTPException(
            status_code=404,
            detail="Vulnerability not found",
        )

    FixedRepository.delete(
        db,
        cve_id,
    )

    FixedRepository.save(db)

    return {
        "message": "Vulnerability unmarked as fixed"
    }