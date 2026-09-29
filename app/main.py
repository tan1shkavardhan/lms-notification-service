from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import AsyncSessionLocal

app = FastAPI(
    title="LMS Notification Service",
    description="Notification service for the LMS",
    version="1.0.0",
)


@app.get("/health")
async def health_check():
    async with AsyncSessionLocal() as session:
        result = await session.execute(text("SELECT 1"))
        database_status = result.scalar()

    return {
        "status": "ok",
        "service": "notification-service",
        "database": database_status,
    }