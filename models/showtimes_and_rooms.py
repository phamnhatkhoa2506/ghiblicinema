from .utils import *

class ShowtimesAndRooms(Base):
    __tablename__ = "showtimes_and_rooms"

    showtime_id = Column(UUID, ForeignKey("showtime.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    room_id = Column(UUID, ForeignKey("room.id", ondelete="CASCADE"), primary_key=True, nullable=False)