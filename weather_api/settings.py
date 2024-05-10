import os
import logging

import dotenv

dotenv.load_dotenv()


class DevConf:
    LOG_LEVEL = getattr(logging, os.environ.get("LOG_LEVEL", "DEBUG"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "database.sqlite3")
    SQLITE3_ECHO = os.environ.get("DATABASE_ECHO", "True") == "True"
    EMAIL = os.environ.get("EMAIL", "example@gmail.com")
    MEMCACHED_HOST = os.environ.get("MEMCACHED_HOST", "127.0.0.1")
    MEMCACHED_PORT = int(os.environ.get("MEMCACHED_PORT", 11211))

    weatherapi_url = (
        "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}"
    )
    weatherapi_headers = {
        "User-Agent": "weather_api/0.1.0",
        "From": EMAIL,
        "Accept-Encoding": "gzip, deflate",
    }


conf = DevConf()
