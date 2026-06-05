import uuid
from sqlalchemy import String,DateTime,func
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime,timezone
from app.database import Base

class User(Base):
    __tablename__="users"

    id:Mapped[uuid.UUID]=mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    name:Mapped[str]=mapped_column(
        String(100),
        nullable=False
    )
    email:Mapped[str]=mapped_column(
        String(225),
        nullable=False,
        unique=True,
        index=True
    )
    hashed_password:Mapped[str]=mapped_column(
        String(225),
        nullable=False
    )
    created_at:Mapped[DateTime]=mapped_column(
       DateTime,
       default=datetime.now(timezone.utc)
    )