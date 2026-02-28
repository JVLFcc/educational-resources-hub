from sqlalchemy import Column, Integer, String, Text
from .db import Base

class Resource(Base):
    __tablename__ = "resources"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    resource_type = Column(String(50), nullable=False)