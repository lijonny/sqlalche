"""add tagname

Revision ID: 2f47d7e1edac
Revises: 0dc9bd3bbaba
Create Date: 2017-11-27 17:45:03.791000

"""
from alembic import op
import sqlalchemy as sa
import os
import sys
#print '1:',sys.path
filepath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(filepath)
#print '2:',sys.path
from alembic_demo import session,Tag
from sqlalchemy import or_
# revision identifiers, used by Alembic.
revision = '2f47d7e1edac'
down_revision = '0dc9bd3bbaba'
branch_labels = None
depends_on = None


def upgrade():
    tag1 = Tag(name='python')
    tag2 = Tag(name='php')
    tag3 = Tag(name='android')
    session.add_all([tag1,tag2,tag3,])
    session.commit()
    #pass


def downgrade():
    tag4 = Tag(name='app')
    tags = session.query(Tag).filter(Tag.name=='android')
    session.add(tag4)
    session.delete(tags)
    print 'ko'
    session.commit()
    #pass
