from collections import namedtuple

from .client_cache import RedisCache, CacheConfig

Plugin = namedtuple("Plugin", ("name", "package", "class_name"))

PLUGINS = {
    "redis_cache": Plugin(".redis_cache", __name__, "RedisCache"),
    "cache_config": Plugin(".redis_cache", __name__, "CacheConfig"),

}

__all__ = ["RedisCache", "CacheConfig"]
