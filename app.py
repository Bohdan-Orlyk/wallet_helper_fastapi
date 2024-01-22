import uvicorn

from fastapi import FastAPI, status

from src.payments.api.payments import payments_router
from src.wallet.api.wallet import wallet_router


app = FastAPI()

ROUTERS = [
    payments_router,
    wallet_router
]

for router in ROUTERS:
    app.include_router(router)


@app.get("/")
def healthcheck():
    return {status.HTTP_200_OK, "OK"}


if __name__ == "__main__":
    uvicorn.run(
        app=app,           # .env
        host="127.0.0.1",  # .env
        port=9876          # .env
    )
