from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()


class News(Base):
    __tablename__ = "new_sheet"
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    link = Column(String)
    author = Column(String)
    updated = Column(String)
    summary = Column(String)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())