from fastapi import FastAPI

app = FastAPI(
    title="LMS Notification Service",
    description="Notification service for the LMS",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "notification-service"
    }