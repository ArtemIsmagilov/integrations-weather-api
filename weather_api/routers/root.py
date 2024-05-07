from fastapi import APIRouter

from weather_api.shemas import PingPong

router = APIRouter(
    prefix="/root",
    tags=["root"],
)


@router.get("/ping")
async def ping_pong() -> PingPong:
    """
    Check health server:
    """
    return PingPong(detail="pong")
