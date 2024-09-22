from .utils import *

class BookingTicketsInfor(Base):
    __tablename__ = "booking_tickets_infor"

    id = Column(UUID, primary_key=True, nullable=False)
    user_id = Column(UUID, ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
    booking_date = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text('NOW()'))
    total_price = Column(Numeric(10, 0), nullable=False)

    # many - 1
    user_relationship = relationship("User", back_populates="booking_tickets_info_relationship")

    # 1 - many
    booking_tickets_relationship = relationship("BookingTickets", back_populates="booking_tickets_info_relationship")