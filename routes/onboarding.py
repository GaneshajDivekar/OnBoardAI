from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import OnboardingTask, User, Document

router = APIRouter()


# ✅ Get User Onboarding Status
@router.get("/onboarding/{user_id}")
def get_onboarding_status(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    tasks = db.query(OnboardingTask).filter(OnboardingTask.user_id == user_id).all()
    documents = db.query(Document).filter(Document.user_id == user_id).all()

    return {
        "name": user.name,
        "email": user.email,
        "onboarding_complete": user.onboarding_complete,
        "tasks": [{"name": t.task_name, "status": t.status} for t in tasks],
        "documents": [{"name": d.document_name, "status": d.status} for d in documents]
    }


# ✅ Update Task Status
@router.put("/onboarding/task/{task_id}")
def update_task_status(task_id: int, status: str, db: Session = Depends(get_db)):
    task = db.query(OnboardingTask).filter(OnboardingTask.id == task_id).first()
    if not task:
        return {"error": "Task not found"}

    task.status = status
    db.commit()
    return {"message": "Task updated successfully"}


# ✅ Upload Document Status
@router.put("/onboarding/document/{doc_id}")
def update_document_status(doc_id: int, status: str, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == doc_id).first()
    if not document:
        return {"error": "Document not found"}

    document.status = status
    db.commit()
    return {"message": "Document updated successfully"}
