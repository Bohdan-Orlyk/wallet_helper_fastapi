from fastapi import APIRouter

wallet_router = APIRouter(
    prefix="/wallet",
    tags=["Wallet"]
)


@wallet_router.get("")
def get_wallet_score():
    pass
