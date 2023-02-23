from domain.dto.base import DTO


class QuoteAuthorDTO(DTO):
    """Quote Author Data Transfer Object"""
    author_id: int
    name: str
