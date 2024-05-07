import aiosqlite
from aiosqlite import Cursor

from weather_api.settings import conf
from weather_api.logger import logger


async def get_db() -> Cursor:
    conn = await aiosqlite.connect(conf.DATABASE_URL)
    conn.row_factory = aiosqlite.Row

    if conf.SQLITE3_ECHO:
        await conn.set_trace_callback(logger.debug)
    try:
        yield await conn.cursor()
    finally:
        await conn.close()
