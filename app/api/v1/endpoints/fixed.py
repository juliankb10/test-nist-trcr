from fastapi import APIRouter
from fastapi import Depends

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

        if not exists:

            FixedRepository.create(
                db,
                cve_id,
            )

    FixedRepository.save(db)

    return {
        "message": "Vulnerabilities marked as fixed"
    }