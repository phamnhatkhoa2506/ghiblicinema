
from .utils import *

class Row(Base):
    __tablename__ = "row"

    id = Column(UUID, primary_key=True, nullable=False)
    alp_char = Column(CHAR, nullable=False)

    #  1 - many
    seat_relationship = relationship("Seat", back_populates="row_relationship")