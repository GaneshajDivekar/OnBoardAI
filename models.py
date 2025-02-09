import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base

# ✅ User Table (Onboarding Status)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    onboarding_complete = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    documents = relationship("Document", back_populates="user")
    tasks = relationship("OnboardingTask", back_populates="user")
    training_progress = relationship("TrainingProgress", back_populates="user")

# ✅ Document Submission Table
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    document_name = Column(String, nullable=False)
    status = Column(String, default="Pending")  # Pending, Approved, Rejected

    user = relationship("User", back_populates="documents")

# ✅ Onboarding Task Tracking Table
class OnboardingTask(Base):
    __tablename__ = "onboarding_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_name = Column(String, nullable=False)
    status = Column(String, default="Pending")  # Pending, Completed

    user = relationship("User", back_populates="tasks")

# ✅ Training Progress Table
class TrainingProgress(Base):
    __tablename__ = "training_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    module = Column(String)
    completion = Column(String, default="Not Started")

    user = relationship("User", back_populates="training_progress")
