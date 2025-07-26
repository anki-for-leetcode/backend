from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from typing import List
from contextlib import asynccontextmanager

from database import async_session, init_db
from models import QuestionCompleted
from schemas import QuestionCompletedBody, QuestionCompletedResponse
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

# Dependency for getting DB session
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    
app = FastAPI(lifespan=lifespan)

@app.post("/completed", response_model=QuestionCompletedResponse)
async def question_completed(
    body: QuestionCompletedBody, 
    session: AsyncSession = Depends(get_session)
):
    stmt = insert(QuestionCompleted).values(id=body.id, question_id=body.question_id, study_plan=body.study_plan, available_in=body.available_in).returning(QuestionCompleted)
    result = await session.execute(stmt)
    question_insert_result = result.scalar_one_or_none()
    if not question_insert_result:
        raise HTTPException(status_code=400, detail="Failed to update question completion")

    await session.commit()
    return question_insert_result  # Pydantic will parse via orm_mode