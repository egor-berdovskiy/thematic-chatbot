from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from typing import Union

from database.models import User, UserType


class AdminFilter(BaseFilter):
    async def __call__(self, event: Union[Message,CallbackQuery], user: User) -> bool:
        if user:
            return user.type == UserType.admin
