import redis
import logging


class RedisCache(object):
    def __init__(self, config):
        self.connection = self.prepare_cache(config)

    def prepare_cache(self, Config):
        client = redis.Redis(
            host=Config.HOST,
            port=Config.PORT,
            password=Config.PASSWD,
            db=Config.DB,
            decode_responses=True,
        )
        # client.flushdb()
        return client

    def cache_get(self, key) -> str:
        return self.connection.get(key)

    def cache_has(self, key) -> bool:
        return self.connection.exists(key)


class CacheConfig(object):
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        self.init_params(config)

    def init_params(self, config):

        for key, value in config.dict().items():
            key = key.upper()
            if not hasattr(self, key):
                setattr(self, key, value)
            else:
                self.logger.info(f'[✗] Ignore duplication attribute "{key}"')
