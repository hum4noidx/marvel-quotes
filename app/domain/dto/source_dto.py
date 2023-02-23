from domain.dto.base import DTO


class SourceDTO(DTO):
    """Quote Source Data Transfer Object"""
    source_id: int
    name: str
