from pydantic import BaseModel

class DocumentCreate(BaseModel):
    name: str

class DocumentUpdate(BaseModel):
    status: str

class TrainingUpdate(BaseModel):
    user_name: str
    module: str
    completion: str

class ChatRequest(BaseModel):
    message: str
