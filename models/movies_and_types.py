from .utils import *

class MoviesAndTypes(Base):
    __tablename__ = "movies_and_types"

    movie_id = Column(UUID, ForeignKey("movie.id", ondelete = "CASCADE"), primary_key=True, nullable=False)
    type_id = Column(UUID, ForeignKey("movie_type.id", ondelete = "CASCADE"), primary_key=True, nullable=False)