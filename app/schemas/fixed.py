from pydantic import BaseModel


class FixedVulnerabilityRequest(BaseModel):
    cve_ids: list[str]