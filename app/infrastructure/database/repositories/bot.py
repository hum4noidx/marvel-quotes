from sqlalchemy import update

from domain import dto
from infrastructure.database.models.bot_status import BotStatus
from infrastructure.database.repositories.repo import SQLAlchemyRepo


class BotRepo(SQLAlchemyRepo):

    async def get_bot_settings(self):
        query = await self.session.get(BotStatus, 1)
        return dto.bot.BotDTO.from_orm(query)

    async def set_maintenance(self):
        await self.session.execute(
            update(BotStatus).where(BotStatus.id == 1).values(status='maintenance')
        )
        await self.session.commit()

    async def disable_maintenance(self):
        await self.session.execute(
            update(BotStatus).where(BotStatus.id == 1).values(status='normal')
        )
        await self.session.commit()
