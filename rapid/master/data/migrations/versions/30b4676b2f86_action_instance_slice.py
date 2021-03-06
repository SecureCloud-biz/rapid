"""
 Copyright (c) 2015 Michael Bright and Bamboo HR LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

action_instance_slice

Revision ID: 30b4676b2f86
Revises: 3da597dde134
Create Date: 2016-01-27 09:03:18.577289

"""

# revision identifiers, used by Alembic.
revision = '30b4676b2f86'
down_revision = '3da597dde134'
branch_labels = ()
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
    if 'sqlite' != op.get_context().dialect.name:
        op.alter_column('action_instances', 'slice',
                   existing_type=mysql.VARCHAR(length=25),
                   nullable=True)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    if 'sqlite' != op.get_context().dialect.name:
        op.alter_column('action_instances', 'slice',
                   existing_type=mysql.VARCHAR(length=25),
                   nullable=False)
        ### end Alembic commands ###
