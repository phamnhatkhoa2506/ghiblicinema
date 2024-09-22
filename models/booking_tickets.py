from .utils import *

class BookingTickets(Base):
    __tablename__ = "booking_tickets"

    id = Column(UUID, primary_key=True, nullable=False)
    booking_id = Column(UUID, ForeignKey("booking_tickets_infor.id", ondelete="CASCADE"),nullable=False)
    ticket_id = Column(UUID, ForeignKey("ticket.id", ondelete="CASCADE"),nullable=False)
    quantity = Column(Integer, nullable=False)

    # many - 1
    booking_tickets_info_relationship = relationship("BookingTicketsInfor", back_populates="booking_tickets_relationship")
    ticket_relationship = relationship("Ticket", back_populates="booking_tickets_relationship")

    # 1 - many
    booking_seats_relationship = relationship("BookingSeats", back_populates="booking_tickets_relationship")