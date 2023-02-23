from sqlalchemy import Column, Integer, String

from infrastructure.database.base import Base


class QuoteSource(Base):
    __tablename__ = 'quote_sources'

    source_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
