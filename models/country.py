from .utils import *

class Country(Base):
    __tablename__ = "country"

    id = Column(UUID, primary_key=True, nullable=False)
    name_vn = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    #  1- many
    movie_relationship = relationship("Movie", back_populates="country_relationship")