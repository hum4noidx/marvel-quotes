from pydantic import parse_obj_as
from sqlalchemy import select

from domain.dto.quote_dto import QuoteDTO
from infrastructure.database.models.author import QuoteAuthor
from infrastructure.database.models.quote import Quote
from infrastructure.database.models.source import QuoteSource
from infrastructure.database.repositories.repo import SQLAlchemyRepo


class QuoteReader(SQLAlchemyRepo):
    async def get_all_quotes(self):
        result = await self.session.execute(
            select(Quote)
        )
        return parse_obj_as(list[QuoteDTO], result.scalars().all())

    async def search_quotes(self, query):
        result = await self.session.execute(
            select(Quote).filter(Quote.quote_en.ilike(f'%{query}%'))
        )
        return parse_obj_as(list[QuoteDTO], result.scalars().all())

    async def get_quote_by_source(self, source):
        result = await self.session.execute(
            select(Quote).filter(Quote.source == QuoteSource.id).filter(QuoteSource.name == source)
        )
        return parse_obj_as(list[QuoteDTO], result.scalars().all())
