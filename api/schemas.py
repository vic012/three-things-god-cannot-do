from pydantic import BaseModel, ConfigDict


class MessageSchema(BaseModel):
	id: int = 0
	text_message: str | None = None
	reference: str | None = None
	active: bool = False

	model_config = ConfigDict(
		from_attribute=True
	)


class MessagesListSchemaResponse(BaseModel):
	results: list[MessageSchema]

	model_config = ConfigDict(
		from_attribute=True
	)


class MessageSchemaCreate(BaseModel):
	text_message: str = "Mensagem"
	reference: str = "Referência"
	active: bool = False

	model_config = ConfigDict(
		from_attribute=True
	)

class MessageSchemaUpdate(BaseModel):
	text_message: str
	reference: str = "Referência"
	active: bool = False
