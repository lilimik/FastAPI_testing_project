import uvicorn

from fastapi import FastAPI

from app.core import settings
from app.api.v1 import api_router
from app.api.hooks import setup_hooks

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)

setup_hooks(app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)
