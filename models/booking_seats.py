from .utils import *

class BookingSeats(Base):
    __tablename__ = "booking_seats"

    id = Column(UUID, primary_key=True, nullable=False)
    booking_tickets_id = Column(UUID, ForeignKey("booking_tickets.id", ondelete="CASCADE"), nullable=False)
    seat_id = Column(UUID, ForeignKey("seat.id", ondelete="CASCADE"), nullable=False)

    # many - 1
    booking_tickets_relationship = relationship("BookingTickets", back_populates="booking_seats_relationship")
    seat_relationship = relationship("Seat", back_populates="booking_seats_relationship")