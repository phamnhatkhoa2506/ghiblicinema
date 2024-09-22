from .utils import *

class Concession(Base):
    __tablename__ = 'concession'

    id = Column(UUID, primary_key = True, nullable = False)
    name_vn = Column(String, nullable = False)
    name_en = Column(String, nullable=False)
    combo = Column(Boolean, nullable = False)
    price = Column(Numeric(10, 0), nullable = False)

    # 1 - many
    booking_concessions_relationship = relationship("BookingConcessions", back_populates="concession_relationship")