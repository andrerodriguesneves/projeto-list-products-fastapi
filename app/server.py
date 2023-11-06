from fastapi import FastAPI
from app.api.products.routes import app_products

app = FastAPI()

app.include_router(app_products)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)