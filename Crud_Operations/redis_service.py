from redis_client import redis_client

class RedisService:
    @staticmethod
    async def set_item(key: str, value: str):
        return await redis_client.set(key, value)

    @staticmethod
    async def get_item(key: str):
        return await redis_client.get(key)

    @staticmethod
    async def update_item(key: str, value: str):
        exists = await redis_client.exists(key)
        if exists:
            return await redis_client.set(key, value)
        return None

    @staticmethod
    async def delete_item(key: str):
        return await redis_client.delete(key)