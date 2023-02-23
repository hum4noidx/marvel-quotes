from datetime import datetime

from domain.dto.base import DTO
from domain.dto.quote_author_dto import QuoteAuthorDTO
from domain.dto.source_dto import SourceDTO


class QuoteDTO(DTO):
    """Quote Data Transfer Object"""
    quote_id: int
    quote_en: str
    author_en: int
    source_en: int
    created_at: datetime
    updated_at: datetime
    author_obj: QuoteAuthorDTO
    source_obj: SourceDTO
