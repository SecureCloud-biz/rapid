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

pipeline_instance_commits

Revision ID: e2a50a08334a
Revises: b3120dbd0b68
Create Date: 2016-03-04 09:38:56.832887

"""

# revision identifiers, used by Alembic.
revision = 'e2a50a08334a'
down_revision = 'b3120dbd0b68'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pipeline_instance_commits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pipeline_instance_id', sa.Integer(), nullable=False),
    sa.Column('commit_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['commit_id'], ['commits.id'], ),
    sa.ForeignKeyConstraint(['pipeline_instance_id'], ['pipeline_instances.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_engine='InnoDB'
    )
    op.create_index(op.f('ix_pipeline_instance_commits_commit_id'), 'pipeline_instance_commits', ['commit_id'], unique=False)
    op.create_index(op.f('ix_pipeline_instance_commits_id'), 'pipeline_instance_commits', ['id'], unique=False)
    op.create_index(op.f('ix_pipeline_instance_commits_pipeline_instance_id'), 'pipeline_instance_commits', ['pipeline_instance_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pipeline_instance_commits_pipeline_instance_id'), table_name='pipeline_instance_commits')
    op.drop_index(op.f('ix_pipeline_instance_commits_id'), table_name='pipeline_instance_commits')
    op.drop_index(op.f('ix_pipeline_instance_commits_commit_id'), table_name='pipeline_instance_commits')
    op.drop_table('pipeline_instance_commits')
    ### end Alembic commands ###
