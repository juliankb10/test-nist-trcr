from sqlalchemy.orm import Session

from app.models.fixed_vulnerability import (
    FixedVulnerability,
)


class FixedRepository:

    @staticmethod
    def get_all_fixed_ids(
        db: Session,
    ) -> set[str]:

        rows = db.query(
            FixedVulnerability
        ).all()

        return {
            row.cve_id
            for row in rows
        }

    @staticmethod
    def exists(
        db: Session,
        cve_id: str,
    ) -> bool:

        return (
            db.query(FixedVulnerability)
            .filter(
                FixedVulnerability.cve_id == cve_id
            )
            .first()
            is not None
        )

    @staticmethod
    def create(
        db: Session,
        cve_id: str,
    ) -> FixedVulnerability:

        fixed = FixedVulnerability(
            cve_id=cve_id
        )

        db.add(fixed)

        return fixed

    @staticmethod
    def save(db: Session):

        db.commit()