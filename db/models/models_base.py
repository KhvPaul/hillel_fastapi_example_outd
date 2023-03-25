import datetime

import sqlalchemy as sa
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship

from pydentic_models import enums

Base = declarative.declarative_base()

_uuid = lambda: uuid.uuid4().hex  # noqa future workpiece for function
generate_uuid = lambda: _uuid()  # noqa


class User(Base):
    __tablename__ = "users"

    id = sa.Column(  # noqa: A003
        "id",
        sa.String(48),
        unique=True,
        nullable=False,
        primary_key=True,
        default=_uuid,
    )
    email = sa.Column("email", sa.String(320), unique=True, nullable=False)
    password = sa.Column("password", sa.Text, nullable=False)

    profile = relationship("UserProfile", uselist=False, viewonly=True)


class UserProfile(Base):
    __tablename__ = "user_profiles"

    user_id = sa.Column(
        "user_id",
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        primary_key=True,
    )
    first_name = sa.Column("first_name", sa.String(255), nullable=False)
    last_name = sa.Column("last_name", sa.String(255), nullable=False)
    birthday = sa.Column("birthday", sa.DATE, nullable=False)
    gender = sa.Column("gender", sa.Enum(enums.Genders), nullable=False)
    phone_number = sa.Column("phone_number", sa.VARCHAR(15), nullable=False)
    created_at = sa.Column("created_at", sa.DateTime, default=datetime.datetime.utcnow)
    updated_at = sa.Column(
        "updated_at", sa.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )