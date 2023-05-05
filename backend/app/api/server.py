from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router


def get_application():
    main = FastAPI(title="MyCleaner", version="1.0.0")

    main.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    main.include_router(api_router, prefix="/api")

    return main


app = get_application()
