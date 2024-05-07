from aiosqlite import (
    Cursor,
    Row,
)
from typing import Iterable


async def get_city_by_name(cur: Cursor, city_name: str) -> Row | None:
    await cur.execute(
        """
        SELECT title, lat, lon FROM cities
        WHERE title=:city_name
        ORDER BY rank
        LIMIT 1
        """,
        {"city_name": city_name},
    )
    return await cur.fetchone()


async def find_cities(cur: Cursor, q: str) -> Iterable[Row]:
    await cur.execute(
        """
        SELECT title FROM cities
        WHERE title MATCH :q
        ORDER BY rank
        """,
        {"q": f"{q}*"},
    )
    return await cur.fetchall()
