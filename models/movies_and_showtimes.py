from .utils import *

class MoviesAndShowtimes(Base):
    __tablename__ = "movies_and_showtimes"

    movie_id = Column(UUID, ForeignKey("movie.id", ondelete = "CASCADE"), primary_key=True, nullable=False)
    showtime_id = Column(UUID, ForeignKey("showtime.id", ondelete = "CASCADE"), primary_key=True, nullable=False)

    