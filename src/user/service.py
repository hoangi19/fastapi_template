from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_db_session
from src.user.model import UserModel


class UserDAO:
    """Class for accessing user table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_user_model(self, name: str) -> None:
        """
        Add single user to session.

        :param name: name of a user.
        """
        self.session.add(UserModel(name=name))

    async def get_all_user(self, limit: int, offset: int) -> List[UserModel]:
        """
        Get all user models with limit/offset pagination.

        :param limit: limit of user.
        :param offset: offset of user.
        :return: stream of user.
        """
        raw_user = await self.session.execute(
            select(UserModel).limit(limit).offset(offset),
        )

        return list(raw_user.scalars().fetchall())

    async def filter(
        self,
        name: Optional[str] = None,
    ) -> List[UserModel]:
        """
        Get specific user model.

        :param name: name of user instance.
        :return: user models.
        """
        query = select(UserModel)
        if name:
            query = query.where(UserModel.name == name)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())
