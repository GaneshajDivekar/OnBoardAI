from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models import Document
from schemas import DocumentCreate, DocumentUpdate

router = APIRouter()

@router.post("/documents/")
async def create_document(doc: DocumentCreate, db: AsyncSession = Depends(get_db)):
    new_doc = Document(name=doc.name)
    db.add(new_doc)
    await db.commit()
    return {"message": "Document submitted successfully"}

@router.get("/documents/")
async def get_documents(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document))
    return result.scalars().all()

@router.put("/documents/{doc_id}")
async def update_document(doc_id: int, doc: DocumentUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Document).where(Document.id == doc_id))
    document = result.scalars().first()
    if document:
        document.status = doc.status
        await db.commit()
        return {"message": "Document status updated"}
    return {"error": "Document not found"}
