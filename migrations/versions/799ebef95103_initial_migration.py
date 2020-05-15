"""initial Migration

Revision ID: 799ebef95103
Revises: 
Create Date: 2020-05-14 12:18:08.392780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '799ebef95103'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_delivery_id'), 'delivery', ['id'], unique=True)
    op.create_table('parcel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_parcel_id'), 'parcel', ['id'], unique=True)
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=True)
    op.create_table('zones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_zones_id'), 'zones', ['id'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identification', sa.Integer(), nullable=True),
    sa.Column('firstName', sa.String(length=255), nullable=True),
    sa.Column('lastName', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('Address', sa.String(), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.Column('contactNumber', sa.String(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('payment_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['payment_name'], ['payment.name'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contactNumber')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_identification'), 'users', ['identification'], unique=True)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('zone', sa.String(), nullable=True),
    sa.Column('destination', sa.String(length=255), nullable=True),
    sa.Column('token', sa.String(length=255), nullable=True),
    sa.Column('totalprice', sa.Integer(), nullable=True),
    sa.Column('ParcelTypeid', sa.Integer(), nullable=True),
    sa.Column('DeliveryTypeid', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('deliveryStatus', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['DeliveryTypeid'], ['delivery.id'], ),
    sa.ForeignKeyConstraint(['ParcelTypeid'], ['parcel.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.identification'], ),
    sa.ForeignKeyConstraint(['zone'], ['zones.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=True)
    op.create_index(op.f('ix_orders_token'), 'orders', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_token'), table_name='orders')
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_users_identification'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_zones_id'), table_name='zones')
    op.drop_table('zones')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    op.drop_table('payment')
    op.drop_index(op.f('ix_parcel_id'), table_name='parcel')
    op.drop_table('parcel')
    op.drop_index(op.f('ix_delivery_id'), table_name='delivery')
    op.drop_table('delivery')
    # ### end Alembic commands ###