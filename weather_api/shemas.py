from datetime import datetime

from pydantic import BaseModel


class PingPong(BaseModel):
    detail: str


class TemperatureCity(BaseModel):
    time: datetime
    celsius: float


class City(BaseModel):
    title: str
