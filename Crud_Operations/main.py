from fastapi import FastAPI, HTTPException
from models import Item
from redis_service import RedisService

app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
    await RedisService.set_item(item.key, item.value)
    return {"message": f"Item '{item.key}' created."}

@app.get("/item/{key}")
async def read_item(key: str):
    value = await RedisService.get_item(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"key": key, "value": value}

@app.put("/item/{key}")
async def update_item(key: str, item: Item):
    result = await RedisService.update_item(key, item.value)
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found for update")
    return {"message": f"Item '{key}' updated."}

@app.delete("/item/{key}")
async def delete_item(key: str):
    deleted = await RedisService.delete_item(key)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found for deletion")
    return {"message": f"Item '{key}' deleted."}
