from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String

from src.base import Base


class UserModel(Base):
    """Model for demo purpose."""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200))  # noqa: WPS432
