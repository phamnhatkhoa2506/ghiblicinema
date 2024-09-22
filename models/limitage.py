from .utils import *

class LimitAge(Base):
    __tablename__ = "limitage"

    id = Column(UUID, primary_key=True, nullable=False)
    name_vn = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    #  1- many
    movie_relationship = relationship("Movie", back_populates="limitage_relationship")