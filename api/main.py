from fastapi import FastAPI
from app.presentation.routes.tasks import router
from core.config.database_config import create_database
import uvicorn

create_database()
app = FastAPI()

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
