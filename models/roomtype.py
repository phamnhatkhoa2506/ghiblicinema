from .utils import *

class RoomType(Base):
    __tablename__ = "room_type"

    id = Column(UUID, primary_key=True, nullable=False)
    name_vn = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    # 1 - many
    room_relationship = relationship("Room", back_populates="room_type_relationship")