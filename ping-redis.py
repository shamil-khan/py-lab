import os
from langchain_community.utilities.redis import get_client

redis_url = os.getenv("REDIS_URL", "redis://redis:6379")
client = get_client(redis_url)
print(f"Connected to Redis: {client.ping()}")
