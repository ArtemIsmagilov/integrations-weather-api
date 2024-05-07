from datetime import datetime

from httpx import (
    Response,
    AsyncClient,
)

from weather_api.settings import conf


async def send_req_weatherapi(
    lat: str, lon: str, if_modified_since: str = None
) -> Response:
    async with AsyncClient() as ac:
        headers = conf.weatherapi_headers.copy()
        if if_modified_since:
            headers["If-Modified-Since"] = if_modified_since
        return await ac.get(conf.weatherapi_url.format(lat, lon), headers=headers)


def extract_celsius_time(data: dict) -> list[dict]:
    return [
        {
            "time": datetime.fromisoformat(s["time"]),
            "celsius": s["data"]["instant"]["details"]["air_temperature"],
        }
        for s in data["properties"]["timeseries"]
        if "12:00:00" in s["time"]
    ]
