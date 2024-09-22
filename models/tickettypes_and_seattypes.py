from .utils import *

class TickettypesAndSeattypes(Base):
    __tablename__ = "tickettypes_and_seattypes"

    ticket_type_id = Column(UUID, ForeignKey("ticket_type.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    seat_type_id = Column(UUID, ForeignKey("seat_type.id", ondelete="CASCADE"), primary_key=True, nullable=False)