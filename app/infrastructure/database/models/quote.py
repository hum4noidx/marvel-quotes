from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.database.base import Base


class Quote(Base):
    __tablename__ = 'quotes'

    quote_id = Column(Integer, primary_key=True, autoincrement=True)
    quote_en = Column(Text, nullable=False)
    quote_ru = Column(Text, nullable=False)
    author_en = Column(ForeignKey('quote_authors.author_id'), nullable=False)
    source_en = Column(ForeignKey('quote_sources.source_id'), nullable=False)
    source_obj = relationship("QuoteSource", lazy="joined", viewonly=True,
                              foreign_keys=[source_en])
    author_obj = relationship("QuoteAuthor", lazy="joined", viewonly=True,
                              foreign_keys=[author_en])
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
