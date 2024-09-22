from .utils import *

class RoomsAndSeats(Base):
    __tablename__ = "rooms_and_seats"

    room_id = Column(UUID, ForeignKey("room.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    seat_id = Column(UUID, ForeignKey("seat.id", ondelete="CASCADE"), primary_key=True, nullable=False)