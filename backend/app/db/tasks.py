import logging

from app.api.core.config import DATABASE_URL
from databases import Database
from fastapi import FastAPI

logger = logging.getLogger(__name__)

'''
The tasks file we've created will establish our database connection and handle any additional configuration we require
'''

async def connect_to_db(app: FastAPI) -> None:
    database = Database(DATABASE_URL, min_size=2 , max_size=10)
    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("---- DB CONNECTION ERROR ----")
        logger.warn(e)
        logger.warn("---- DB CONNECTION ERROR ----")

async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("---- DB CONNECTION ERROR ----")
        logger.warn(e)
        logger.warn("---- DB CONNECTION ERROR ----")

