from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class QuestionCompleted(Base):
    __tablename__ = "questions_completed"

    id = Column(String, primary_key=True)
    question_id = Column(Integer, nullable=False)
    study_plan = Column(String, nullable=False)
    available_in = Column(DateTime(timezone=True), nullable=False)