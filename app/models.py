from uuid import uuid4

from sqlalchemy import Column, UUID, JSON
from sqlalchemy.ext.mutable import MutableDict

from app.database import Base


class Text(Base):
    __tablename__ = "text"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    content = Column("content", MutableDict.as_mutable(JSON))