from .utils import *

class Room(Base):
    __tablename__ = "room"

    id = Column(UUID, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    type_id = Column(UUID, ForeignKey("room_type.id", ondelete="CASCADE"), nullable=False)
    type_name = Column(String, nullable=False)

    # many - 1
    room_type_relationship = relationship("RoomType", back_populates="room_relationship")

    # 1 - many
    ticket_relationship = relationship("Ticket", back_populates="room_relationship")

    # many - many
    showtime_relationship = relationship("Showtime", secondary="showtimes_and_rooms", back_populates="room_relationship")
    seat_relationship = relationship("Seat", secondary="rooms_and_seats", back_populates="room_relationship")