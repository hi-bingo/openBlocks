"""empty message

Revision ID: a6caf0cbb3f7
Revises: e6012c054f8f
Create Date: 2017-11-24 13:46:58.174371

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a6caf0cbb3f7'
down_revision = 'e6012c054f8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projectBase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('fullName', sa.String(length=255), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('whitepaper', sa.String(length=255), nullable=True),
    sa.Column('desp', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('projectGit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('gitAddress', sa.String(length=255), nullable=True),
    sa.Column('star', sa.Integer(), nullable=True),
    sa.Column('forks', sa.Integer(), nullable=True),
    sa.Column('openIssue', sa.Integer(), nullable=True),
    sa.Column('releases', sa.Integer(), nullable=True),
    sa.Column('contributors', sa.Integer(), nullable=True),
    sa.Column('lastCommit', sa.DateTime(), nullable=True),
    sa.Column('weekCommit', sa.Integer(), nullable=True),
    sa.Column('monthCommit', sa.Integer(), nullable=True),
    sa.Column('seasonCommit', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('projectPrice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('supply', sa.BigInteger(), nullable=True),
    sa.Column('amount', sa.String(length=255), nullable=True),
    sa.Column('currentPriceCNY', sa.DECIMAL(precision=10, scale=10), nullable=True),
    sa.Column('marketPriceCNY', sa.DECIMAL(precision=10, scale=10), nullable=True),
    sa.Column('currentPriceUSD', sa.DECIMAL(precision=10, scale=10), nullable=True),
    sa.Column('marketPriceUSD', sa.DECIMAL(precision=10, scale=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('projectgit')
    op.drop_table('projectbase')
    op.drop_table('projectprice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projectprice',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('supply', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('amount', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('currentPriceCNY', mysql.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('marketPriceCNY', mysql.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('currentPriceUSD', mysql.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('marketPriceUSD', mysql.DECIMAL(precision=10, scale=0), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('projectbase',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('fullName', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('website', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('whitepaper', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('desp', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('projectgit',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('gitAddress', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('star', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('forks', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('openIssue', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('releases', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('contributors', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('lastCommit', mysql.DATETIME(), nullable=True),
    sa.Column('weekCommit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('monthCommit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('seasonCommit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('projectPrice')
    op.drop_table('projectGit')
    op.drop_table('projectBase')
    # ### end Alembic commands ###
