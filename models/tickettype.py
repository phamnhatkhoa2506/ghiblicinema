from .utils import *

class TicketType(Base):
    __tablename__ = "ticket_type"

    id = Column(UUID, primary_key=True, nullable=False)
    name_vn = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    # 1 - many
    ticket_relationship = relationship("Ticket", back_populates="ticket_type_relationship")

    # many - many
    seat_type_relationship = relationship("SeatType", secondary="tickettypes_and_seattypes", back_populates="ticket_type_relationship")