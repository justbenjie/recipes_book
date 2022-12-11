from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text
from sqlalchemy.orm import relationship


class Recipe(Base):
    # sqlalchemy model: defines the columns of table within database
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    directions = Column(String, nullable=False)
    calories = Column(Integer, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
