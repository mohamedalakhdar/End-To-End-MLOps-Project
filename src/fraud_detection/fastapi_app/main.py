from fastapi import FastAPI

from .routes import fraud_dect

app = FastAPI(title="Fraud Detection API")
app.include_router(fraud_dect.fraud_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
