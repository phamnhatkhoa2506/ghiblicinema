from .utils import *

class BookingConcessions(Base):
    __tablename__ = "booking_concessions"

    id = Column(UUID, primary_key=True, nullable=False)
    booking_id = Column(UUID, ForeignKey("booking_concessions_infor.id", ondelete="CASCADE"),nullable=False)
    concession_id = Column(UUID, ForeignKey("concession.id", ondelete="CASCADE"),nullable=False)
    quantity = Column(Integer, nullable=False)

    # many - 1
    booking_concessions_info_relationship = relationship("BookingConcessionsInfor", back_populates="booking_concessions_relationship")
    concessions_relationship = relationship("Concession", back_populates="booking_concessions_relationship")