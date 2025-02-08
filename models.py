from sqlalchemy import Column, Integer, String
from database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, default="Pending")

class TrainingProgress(Base):
    __tablename__ = "training_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    module = Column(String)
    completion = Column(String, default="Not Started")
