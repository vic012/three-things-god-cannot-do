from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi import HTTPException

from .models import Message
from .schemas import MessageSchemaCreate, MessageSchemaUpdate


def get_messages(db: Session, skip: int = 0, limit: int = 100):
	return db.query(Message).offset(skip).limit(limit).all()

def get_message(db: Session, message_id: int):
	return db.query(Message).filter(Message.id == message_id).first()

def create_message(db: Session, message: MessageSchemaCreate):
	message_queryset = db.scalar(
		select(Message).where(
			(Message.text_message == message.text_message)
		)
	)
	if message_queryset:
		raise HTTPException(
			status_code=HTTPStatus.BAD_REQUEST,
			detail="Message text alredy exists"
		)

	db_message = Message(
		text_message=message.text_message,
		reference=message.reference,
		active=message.active,
	)
	db.add(db_message)
	db.commit()
	db.refresh(db_message)

	return db_message

def update_message(
	db: Session,
	message_id: int,
	message_data: MessageSchemaUpdate
):

	db_message = get_message(db=db, message_id=message_id)

	if not db_message:
		raise HTTPException(
			status_code=HTTPStatus.NOT_FOUND,
			detail=f"A Menssagem com o ID: {message_id} não existe"
		)

	for key, value in message_data.model_dump(exclude_unset=True).items():
		setattr(db_message, key, value)

	db.add(db_message)
	db.commit()
	db.refresh(db_message)

	return db_message

def delete_message(
	db: Session,
	message_id: int
):

	db_message = get_message(db=db, message_id=message_id)

	if not db_message:
		raise HTTPException(
			status_code=HTTPStatus.NOT_FOUND,
			detail=f"A Menssagem com o ID: {message_id} não existe"
		)

	db.delete(db_message)
	db.commit()

	return {"detail": f"A mensagem com ID: {message_id} foi deletada"}
