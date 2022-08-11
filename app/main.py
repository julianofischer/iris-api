import logging
from starlette.responses import RedirectResponse
from fastapi import FastAPI, Request
from joblib import load
from pydantic import BaseModel


class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    flower_type: str = None

SVC = load('app/iris_classifier.joblib')

app = FastAPI()
logging.basicConfig(filename='log.log', level=logging.INFO)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Request received  [url]: {request.url.path} [host]: {request.client.host}")
    response = await call_next(request)

    if response.status_code == 200:
        logging.info(f"Response returned [status code]: {response.status_code}")
    else:
        logging.error(f"Response returned [status code]: {response.status_code}")
    return response

@app.get("/")
async def root():
    #return {"message": "Hello world!"}
    return RedirectResponse(url="/docs")

@app.post("/predict")
async def predict(flower: Flower):
    f = [[flower.sepal_length, flower.sepal_width, flower.petal_length, flower.petal_width]]
    p = SVC.predict(f)
    flower.flower_type = p[0]
    logging.info(f"[Predicted value]: {flower.flower_type}")
    return flower
