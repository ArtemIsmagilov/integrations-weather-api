from meta_memcache import (
    ServerAddress,
    CacheClient,
    connection_pool_factory_builder,
)

from weather_api.settings import conf

pool = CacheClient.cache_client_from_servers(
    servers=[
        ServerAddress(host=conf.MEMCACHED_HOST, port=conf.MEMCACHED_PORT),
    ],
    connection_pool_factory_fn=connection_pool_factory_builder(),
)


def set_city(city_name: str, time_cels_list: list[dict], ttl: int) -> bool:
    return pool.set(city_name, time_cels_list, ttl)


def get_city(city_name: str) -> list[dict] | None:
    return pool.get(city_name)
