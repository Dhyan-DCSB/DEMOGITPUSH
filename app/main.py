from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Application",
    version="1.0.0",
    description="This is a sample FastAPI application.",
)

data = {"name": "More Data", "value": 7}


@app.get("/")
async def read_root():
    return {"message": "Wlcome to the FastAPI application!"}


@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}


@app.put("/update_data/{item_value}")
async def update_data(item_value: int, new_value: int):
    if item_value != data["value"]:
        return {"error": "Item not found"}
    data["value"] = new_value
    return {"message": "Data updated successfully", "data": data}


@app.delete("/delete_data/{item_value}")
async def delete_data(item_value: int):
    if item_value != data["value"]:
        return {"error": "Item not found"}
    data.clear()
    return {"message": "Data deleted successfully"}
