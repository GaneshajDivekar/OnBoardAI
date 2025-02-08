from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models import TrainingProgress
from schemas import TrainingUpdate

router = APIRouter()

@router.post("/training/")
async def update_training_progress(training: TrainingUpdate, db: AsyncSession = Depends(get_db)):
    new_entry = TrainingProgress(user_name=training.user_name, module=training.module, completion=training.completion)
    db.add(new_entry)
    await db.commit()
    return {"message": "Training progress updated"}

@router.get("/training/")
async def get_training_progress(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TrainingProgress))
    return result.scalars().all()
