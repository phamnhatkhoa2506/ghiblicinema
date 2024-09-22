from .utils import *

class Showtime(Base):
    __tablename__ = "showtime"

    id = Column(UUID, primary_key=True, nullable=False)
    time = Column(String(5), nullable=False)
    date = Column(Date, nullable=False)

    # 1 - many
    ticket_relationship = relationship("Ticket", back_populates="showtime_relationship")

    # many - many
    room_relationship = relationship("Room", secondary="showtimes_and_rooms", back_populates="showtime_relationship")
    movie_relationship = relationship("Movie", secondary="movies_and_showtimes", back_populates="showtime_relationship")