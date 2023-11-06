from fastapi import APIRouter

app_products = APIRouter()

@app_products.get("/products")
async def get_products():
    return {"message": "Hello World from Products"}