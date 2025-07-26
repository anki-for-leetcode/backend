from pydantic import BaseModel
from datetime import datetime

class QuestionCompletedBody(BaseModel):
    id: str
    question_id: int
    study_plan: str
    available_in: datetime

class QuestionCompletedResponse(QuestionCompletedBody):
    id: str

    class Config:
        orm_mode = True