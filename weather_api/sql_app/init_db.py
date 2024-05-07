import asyncio

from weather_api.sql_app.database import get_db


async def main():
    async for cur in get_db():
        with open("./weather_api/sql_app/sql_files/create_table_cities.sql") as f:
            data = f.read()
        await cur.executescript(data)


if __name__ == "__main__":
    asyncio.run(main())
