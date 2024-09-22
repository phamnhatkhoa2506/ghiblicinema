from .utils import *

class MovieType(Base):
    __tablename__ = "movie_type"

    id = Column(UUID, primary_key=True, nullable=False)
    name_vn = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    # many - many
    movie_relationship = relationship("Movie", secondary="movies_and_types", back_populates="movie_type_relationship")
