from .utils import *

class UserRole(enum.Enum):
    admin = "admin"
    editor = "editor"
    user = "user"

class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key = True, nullable = False)
    full_name = Column(String, nullable = False)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    email = Column(String, nullable = False)
    birth_day = Column(Date, nullable = False)
    gender = Column(String, nullable = False)
    phone_number = Column(String, nullable = False)
    identical_id = Column(String, nullable = False)
    role = Column(Enum(UserRole), nullable=False, server_default="user")
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('NOW()'))

    # 1 - many
    booking_concessions_info_relationship = relationship("BookingConcessionsInfor", back_populates="user_relationship")
    booking_tickets_info_relationship = relationship("BookingTicketsInfor", back_populates="user_relationship")