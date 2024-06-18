from typing import Any
from http import HTTPStatus

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends

import api.schemas as schemas
import api.crud as crud
from api.database import get_session
from api.dependencies import get_token_header
from api.models import Message

router = APIRouter(
	prefix="/messages",
	tags=["Mensagens"],
	dependencies=[Depends(get_token_header)],
	responses={404: {"description": "Not found"}},
)

@router.get("/messages", response_model=schemas.MessagesListSchemaResponse)
def get_messages(
	skip: int = 0,
	limit: int = 100,
	session: Session = Depends(get_session),
):
	results = {"results": crud.get_messages(session, skip, limit)}
	return results
	

@router.get("/message/{message_id}")
def get_message(
	message_id: int,
	session: Session = Depends(get_session)
):
	message_data = crud.get_message(session, message_id)

	if not message_data:
		return {"error": f"A mensagem com o ID: {message_id} não existe"}

	return crud.get_message(session, message_id)

@router.post(
	"/message",
	status_code=HTTPStatus.CREATED,
	response_model=schemas.MessageSchema
)
def create_message(
	message: schemas.MessageSchemaCreate,
	session: Session = Depends(get_session)
):
	return crud.create_message(session, message)

@router.patch("/message/{message_id}", response_model=schemas.MessageSchema)
def update_message(
	message_id: int,
	message_data: schemas.MessageSchemaUpdate,
	session: Session = Depends(get_session)
):
	return crud.update_message(session, message_id, message_data)
