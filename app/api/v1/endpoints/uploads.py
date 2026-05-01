import uuid

from pathlib import Path

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File


router = APIRouter()

UPLOAD_DIR = Path(
    "app/uploads/files"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


@router.post("/uploads")
async def upload_file(
    file: UploadFile = File(...),
):

    file_id = str(uuid.uuid4())

    filename = (
        f"{file_id}-{file.filename}"
    )

    file_path = (
        UPLOAD_DIR / filename
    )

    with open(
        file_path,
        "wb",
    ) as buffer:

        content = await file.read()

        buffer.write(content)

    return {
        "id": file_id,
        "url": f"/files/{filename}",
    }