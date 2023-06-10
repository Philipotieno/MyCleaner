from app.api.routes import router as api_router
from app.api.tasks import create_start_app_handler, create_stop_app_handler
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.core.config import PROJECT_NAME, VERSION


def get_application():
    main = FastAPI(title=PROJECT_NAME , version=VERSION)

    main.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    main.add_event_handler("startup", create_start_app_handler(main))
    main.add_event_handler("shutdown", create_stop_app_handler(main))

    main.include_router(api_router, prefix="/api")

    return main


app = get_application()
