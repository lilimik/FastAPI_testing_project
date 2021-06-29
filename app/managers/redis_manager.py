import aioredis


class RedisManager:

    def __init__(self):
        self.pool = None

    async def create_pool(self):
        self.pool = await aioredis.create_redis_pool('redis://localhost')

    async def close_pool(self):
        await self.pool.close()
