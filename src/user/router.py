from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from src.user.model import UserModel
from src.user.schema import UserModelDTO, UserModelInputDTO
from src.user.service import UserDAO

router = APIRouter()


@router.get("/", response_model=List[UserModelDTO])
async def get_user_models(
    limit: int = 10,
    offset: int = 0,
    user_dao: UserDAO = Depends(),
) -> List[UserModel]:
    """
    Retrieve all user objects from the database.

    :param limit: limit of user objects, defaults to 10.
    :param offset: offset of user objects, defaults to 0.
    :param user_dao: DAO for user models.
    :return: list of user objects from database.
    """
    return await user_dao.get_all_user(limit=limit, offset=offset)


@router.put("/")
async def create_user_model(
    new_user_object: UserModelInputDTO,
    user_dao: UserDAO = Depends(),
) -> None:
    """
    Creates user model in the database.

    :param new_user_object: new user model item.
    :param user_dao: DAO for user models.
    """
    await user_dao.create_user_model(**new_user_object.dict())
