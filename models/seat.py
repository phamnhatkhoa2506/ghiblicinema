from .utils import *

class Seat(Base):
    __tablename__ = "seat"

    id = Column(UUID, primary_key=True, nullable=False)
    row_id = Column(UUID, ForeignKey("row.id", ondelete="CASCADE"), nullable=False)
    column_id = Column(UUID, ForeignKey("column.id", ondelete="CASCADE"), nullable=False)
    type_id = Column(UUID, ForeignKey("seat_type.id", ondelete="CASCADE"), nullable=False)
    status = Column(Integer, nullable=False)
    sort_order = Column(Integer, nullable=False)

    # many - 1
    column_relationship = relationship("Column", back_populates="seat_relationship")
    row_relationship = relationship("Row", back_populates="seat_relationship")
    seat_type_relationship = relationship("SeatType", back_populates="seat_relationship")

    # 1 - many
    booking_seats_relationship = relationship("BookingSeats", back_populates="seat_relationship")

    # many-many
    room_relationship = relationship("Room", secondary="rooms_and_seats", back_populates="seat_relationship")
