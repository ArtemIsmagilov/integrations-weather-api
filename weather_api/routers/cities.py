from typing import Annotated
from datetime import (
    datetime,
    UTC,
)

from fastapi import (
    APIRouter,
    Path,
    HTTPException,
    status,
    Query,
    Depends,
)
from aiosqlite import Cursor

from weather_api import (
    details,
    simply_procedures,
)
from weather_api.schemas import (
    TemperatureCity,
    City,
)
from weather_api.simply_procedures import extract_celsius_time
from weather_api.sql_app import crud
from weather_api.sql_app.database import get_db
from weather_api.cached_app import caching

router = APIRouter(
    prefix="/cities",
    tags=["cities"],
)


@router.get("/temperature/{city_name:str}")
async def temperature_city(
    city_name: Annotated[
        str,
        Path(
            min_length=1,
            max_length=155,
            title="City name",
            description="Path description",
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** city_name works correctly.",
                    "value": "Москва",
                },
            },
        ),
    ],
    cur: Annotated[Cursor, Depends(get_db)],
) -> list[TemperatureCity]:
    """
        Get information about temperature only 10 days in current city:

    - **city_name**: title city, require
    """
    if cached_city := caching.get_city(city_name):
        return [TemperatureCity(**i) for i in cached_city]

    city = await crud.get_city_by_name(cur, city_name)
    if city is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=details.city_not_found(city_name),
        )

    response = await simply_procedures.send_req_weatherapi(city["lat"], city["lon"])

    header_expires = response.headers.get("expires")
    # header_last_modified = response.headers.get("last-modified")

    dt_expires = datetime.strptime(header_expires, "%a, %d %b %Y %H:%M:%S %Z").replace(
        tzinfo=UTC
    )

    ttl_expires = int((dt_expires - datetime.now(UTC)).total_seconds())
    if response.status_code == status.HTTP_200_OK:
        result = extract_celsius_time(response.json())
        caching.set_city(city_name, result, ttl_expires)
        return [TemperatureCity(**i) for i in result]

    # elif response.status_code == status.HTTP_304_NOT_MODIFIED:
    #     ...

    else:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=details.status_code_not_200(str(response.url), response.status_code),
        )


@router.get("/search")
async def search_cities(
    q: Annotated[
        str,
        Query(
            min_length=1,
            max_length=155,
            title="Search cities",
            description="Query description",
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** search_cities works correctly.",
                    "value": "М",
                },
            },
        ),
    ],
    cur: Annotated[Cursor, Depends(get_db)],
) -> list[City]:
    """
        Find all cities which were found by 'q':

    - **q**: search with prefix by name cities
    """
    if result := [City(title=row["title"]) for row in await crud.find_cities(cur, q)]:
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=details.city_not_found(q),
    )
