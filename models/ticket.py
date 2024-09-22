from .utils import *

class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(UUID, primary_key=True, nullable=False)
    type_id = Column(UUID, ForeignKey("ticket_type.id", ondelete="CASCADE"), nullable=False)
    movie_id = Column(UUID, ForeignKey("movie.id", ondelete="CASCADE"),nullable=False)
    showtime_id = Column(UUID, ForeignKey("showtime.id", ondelete="CASCADE"),nullable=False)
    room_id = Column(UUID, ForeignKey("room.id", ondelete="CASCADE"), nullable=False)
    price = Column(Numeric(10, 0), nullable=False);

    # many - 1
    ticket_type_relationship = relationship("TicketType", back_populates="ticket_relationship")
    movie_relationship = relationship("Movie", back_populates="ticket_relationship")
    showtime_relationship = relationship("Showtime", back_populates="ticket_relationship")
    room_relationship = relationship("Room", back_populates="ticket_relationship")

    # 1 - many
    booking_tickets_relationship = relationship("BookingTickets", back_populates="ticket_relationship")