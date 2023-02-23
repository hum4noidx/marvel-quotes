from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from infrastructure.database.base import Base


class QuoteAuthor(Base):
    __tablename__ = 'quote_authors'
    author_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    # quotes = relationship("Quote", back_populates="author")
