from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def get_application():
    main = FastAPI(title="MyCleaner", version="1.0.0")

    main.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return main


app = get_application()
