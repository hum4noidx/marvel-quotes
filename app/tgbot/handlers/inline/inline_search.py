import logging
import uuid

from aiogram import Router, types, F

from domain.dto.quote_dto import QuoteDTO
from infrastructure.database.repositories.quote import QuoteReader

logger = logging.getLogger(__name__)
inline_router = Router()


@inline_router.inline_query(F.query.len() > 3)
async def fetch_inline(inline_query: types.InlineQuery, quote_reader: QuoteReader):
    """
    Inline query handler for searching quotes
    """
    logger.info(f'Inline query: {inline_query.id} by {inline_query.from_user.id} - {inline_query.from_user.username}', )
    quotes: list[QuoteDTO] = await quote_reader.search_quotes(inline_query.query)
    search_items = []
    for quote in quotes:
        result_id = str(uuid.uuid4())
        quote_en = quote.quote_en
        quote_source = quote.source_obj.name
        quote_author_en = quote.author_obj.name

        item = types.InlineQueryResultArticle(
            id=result_id,
            title=quote_en,
            description=quote_author_en,
            input_message_content=types.InputTextMessageContent(
                message_text=f'<i>"{quote_en}"</i> - {quote_source}, {quote_author_en}',
                disable_web_page_preview=True
            ),
        )
        search_items.append(item)
    await inline_query.answer(search_items, cache_time=0, is_personal=True)
    logger.info('Inline query: %s is answered.', inline_query.id)


@inline_router.inline_query()
async def fetch_inline(inline_query: types.InlineQuery, quote_reader: QuoteReader):
    """
    Inline query handler for all quotes
    """
    logger.info('Inline query: %s', inline_query.id)
    quotes: list[QuoteDTO] = await quote_reader.get_all_quotes()
    items = []
    for quote in quotes:
        result_id = str(uuid.uuid4())
        quote_en = quote.quote_en
        quote_source = quote.source_obj.name
        quote_author_en = quote.author_obj.name

        item = types.InlineQueryResultArticle(
            id=result_id,
            title=quote_en,
            description=quote_author_en,
            input_message_content=types.InputTextMessageContent(
                message_text=f'<i>"{quote_en}"</i> - {quote_source}, {quote_author_en}',
                disable_web_page_preview=True
            ),
        )
        items.append(item)
    await inline_query.answer(items, cache_time=0, is_personal=True)
    logger.info('Inline query: %s is answered.', inline_query.id)
