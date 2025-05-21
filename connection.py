import redis
from dotenv import load_dotenv
import json
import os

load_dotenv()

r = redis.Redis(
    host = os.getenv("REDIS_URL"),
    port = 6379,
    password = os.getenv("REDIS_TOKEN"),
    ssl = True
)

# r.set('foo','bar')

# Creating a user Json Doc
user_data = {
    "name":"Alice",
    "email":"alice@yahoo.com"
}

#Serialize dict to json string
r.set("user:1", json.dumps(user_data))

# To retrieve
user = json.loads(r.get("user:1"))
print(user)