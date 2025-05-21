import redis.asyncio as redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_url = os.getenv("REDIS_URL")
if not redis_url:
    raise ValueError("Missing REDIS_URL in environment variables")

redis_client = redis.from_url(redis_url, decode_responses=True)
