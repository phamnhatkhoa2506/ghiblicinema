from .utils import *

class Movie(Base):
    __tablename__ = "movie"

    id           = Column(UUID,                                                                         nullable = False, primary_key = True)
    name_vn      = Column(String,                                                                       nullable = False                    )
    name_en      = Column(String,                                                                       nullable = False                    )
    director     = Column(String,                                                                       nullable = False                    )
    actor        = Column(String,                                                                       nullable = False                    )
    release_date = Column(TIMESTAMP(timezone = False),                                                  nullable = False                    )
    end_date     = Column(TIMESTAMP(timezone = False),                                                  nullable = False                    )
    brief_vn     = Column(String,                                                                       nullable = False                    )
    brief_en     = Column(String,                                                                       nullable = False                    )
    image        = Column(String,                                                                       nullable = False                    )
    trailer      = Column(String,                                                                       nullable = False                    )
    status       = Column(Integer,                                                                      nullable = False                    )
    time         = Column(Integer,                                                                      nullable = False                    )
    sortorder    = Column(Integer,                                                                      nullable = False                    )
    country_id   = Column(UUID,                        ForeignKey("country.id", ondelete = "CASCADE") , nullable = False                    )
    format_id    = Column(UUID,                        ForeignKey("format.id", ondelete = "CASCADE")  , nullable = False                    )
    limitage_id  = Column(UUID,                        ForeignKey("limitage.id", ondelete = "CASCADE"), nullable = False                    )
    language_id  = Column(UUID,                        ForeignKey("language.id", ondelete = "CASCADE"), nullable = False                    )
    
    # many - 1
    country_relationship = relationship("Country", back_populates="movie_relationship")
    format_relationship = relationship("Format", back_populates="movie_relationship")
    language_relationship = relationship("Language", back_populates="movie_relationship")
    limitage_relationship = relationship("LimitAge", back_populates="movie_relationship")

    # 1 - many
    ticket_relationship = relationship("Ticket", back_populates="movie_relationship")

    # many - many
    movie_type_relationship = relationship("MovieType", secondary="movies_and_types", back_populates="movie_relationship")
    showtime_relationship = relationship("Showtime", secondary="movies_and_showtimes", back_populates="movie_relationship")