
from .utils import *

class Column(Base):
    __tablename__ = "column"

    id = Column(UUID, primary_key=True, nullable=False)
    number = Column(CHAR, nullable=False)

    #  1 - many
    seat_relationship = relationship("Seat", back_populates="column_relationship")