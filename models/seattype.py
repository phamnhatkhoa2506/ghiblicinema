from .utils import *

class SeatType(Base):
    __tablename__ = "seat_type"

    id = Column(UUID, primary_key=True, nullable=False)
    name_vn = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    # 1 - many
    seat_relationship = relationship("Seat", back_populates="seat_type_relationship")

    # many - many
    ticket_type_relationship = relationship("TicketType", secondary="tickettypes_and_seattypes", back_populates="seat_type_relationship")