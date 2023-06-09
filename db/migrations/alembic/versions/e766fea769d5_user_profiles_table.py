"""user_profiles_table

Revision ID: e766fea769d5
Revises: aa3921a64312
Create Date: 2023-03-25 09:12:49.503616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e766fea769d5'
down_revision = 'aa3921a64312'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user_profiles",
        sa.Column("user_sub", sa.String(length=48), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("birthday", sa.DATE(), nullable=False),
        sa.Column(
            "gender",
            sa.Enum(
                "Male",
                "Female",
                "Other",
                name="genders",
            ),
            nullable=False
        ),
        sa.Column("phone_number", sa.VARCHAR(length=15), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(["user_sub"], ["users.sub"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_sub"),
        sa.UniqueConstraint("user_sub"),
    )


def downgrade() -> None:
    op.drop_table("user_profiles")
    op.execute("DROP TYPE genders;")
