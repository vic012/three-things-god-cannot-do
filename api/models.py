from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, registry


table_registry = registry()


@table_registry.mapped_as_dataclass
class Message:
	__tablename__ = "messages"

	id: Mapped[int] = mapped_column(init=False, primary_key=True)
	text_message: Mapped[str] = mapped_column(String(250))
	reference: Mapped[str] = mapped_column(String(100), nullable=True)
	active: Mapped[bool] = mapped_column(init=True)
