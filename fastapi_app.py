from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from graylog_logger import setup_logger

app = FastAPI()

# Set up the logger
logger = setup_logger()

@app.middleware("http")
async def log_requests(request: fastapi_logger.RequestLogger):
    logger.info(
        f"Request - Method: {request.method}, URL: {request.url}, Status Code: {request.status_code}"
    )
    response = await request.call_next()
    logger.info(
        f"Response - Method: {request.method}, URL: {request.url}, Status Code: {response.status_code}"
    )
    return response

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello, FastAPI with Graylog!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    logger.info(f"Item {item_id} requested with query parameter: {q}")
    return {"item_id": item_id, "q": q}
