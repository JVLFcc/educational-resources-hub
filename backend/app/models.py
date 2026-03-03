from sqlalchemy import Column, Integer, String, Text, JSON
from .db import Base

class Resource(Base):
    __tablename__ = "resources"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    resource_type = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)
    tags = Column(JSON, nullable=True)