from typing_extensions import Annotated
from fastapi import Header, HTTPException
from .config import get_settings


async def get_token_header(x_token: Annotated[str, Header()]):
	settings = get_settings()
	token = settings.token_api
	if x_token != token:
		raise HTTPException(status_code=400, detail="Invalid Token")