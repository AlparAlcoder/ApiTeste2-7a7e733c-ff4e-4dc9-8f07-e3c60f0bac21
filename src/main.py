from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

items = []

@app.post("/items/")
async def create_item(item: Item):
    """
    Create an item
    """
    items.append(item.dict())
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Get an item by id
    """
    if item_id-1 >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id-1]

@app.patch("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Update an item by id
    """
    if  item_id-1 >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id-1] = item.dict()
    return item