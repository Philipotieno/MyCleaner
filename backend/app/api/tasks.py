from fastapi import FastAPI
from app.db.tasks import close_db_connection, connect_to_db

'''
Used to wrap the startup and shutdown events for our app.
'''

def create_start_app_handler(app: FastAPI) -> callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app

def create_stop_app_handler(app: FastAPI) -> callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app