import uvicorn

from fastapi import FastAPI, status
from pydantic import BaseModel

from src.payments.api.payments import payments_router
from src.wallet.api.wallet import wallet_router


app = FastAPI()


class HealthcheckResponse(BaseModel):
    status: int = status.HTTP_200_OK
    message: str = "OK"


@app.get("/", response_model=HealthcheckResponse)
def healthcheck() -> dict:
    return {}


if __name__ == "__main__":

    ROUTERS = [
        payments_router, wallet_router,
    ]

    [app.include_router(router) for router in ROUTERS]

    uvicorn.run(app=app, host="127.0.0.1", port=9876)  # .env
