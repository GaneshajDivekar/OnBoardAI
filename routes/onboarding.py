from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select  # ✅ Import async select

from database import get_db
from models import User, Document, OnboardingTask

router = APIRouter()


# ✅ Get User Onboarding Status
@router.get("/onboarding/{user_id}")
async def get_onboarding_status(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()

    if not user:
        return {"error": "User not found"}

    result_tasks = await db.execute(select(OnboardingTask).filter(OnboardingTask.user_id == user_id))
    tasks = result_tasks.scalars().all()

    result_docs = await db.execute(select(Document).filter(Document.user_id == user_id))
    documents = result_docs.scalars().all()

    return {
        "name": user.name,
        "email": user.email,
        "onboarding_complete": user.onboarding_complete,
        "tasks": [{"name": t.task_name, "status": t.status} for t in tasks],
        "documents": [{"name": d.document_name, "status": d.status} for d in documents]
    }


# ✅ Update Task Status
@router.put("/onboarding/task/{task_id}")
async def update_task_status(task_id: int, status: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(OnboardingTask).filter(OnboardingTask.id == task_id))
    task = result.scalars().first()

    if not task:
        return {"error": "Task not found"}

    task.status = status
    await db.commit()
    return {"message": "Task updated successfully"}


# ✅ Upload Document Status
@router.put("/onboarding/document/{doc_id}")
async def update_document_status(doc_id: int, status: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document).filter(Document.id == doc_id))
    document = result.scalars().first()

    if not document:
        return {"error": "Document not found"}

    document.status = status
    await db.commit()
    return {"message": "Document updated successfully"}
