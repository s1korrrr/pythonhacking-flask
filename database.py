from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, create_session


engine = None
db_session = scoped_session(lambda: create_session(autocommit=False,
                                                   autoflush=False,
                                                   bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_engine(db_uri):
    global engine
    engine = create_engine(db_uri, convert_unicode=True)



def init_db():
    import models.car
    import models.owner
    Base.metadata.create_all(bind=engine)
