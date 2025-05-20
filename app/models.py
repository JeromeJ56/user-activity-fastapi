from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime
from sqlalchemy.orm import relationship
from typing import Dict
from sqlalchemy.dialects.postgresql import JSON

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,nullable=False)
    username = Column(String, index=True,unique=True,nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')) 
    meta_data = Column(JSON)
    # created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


