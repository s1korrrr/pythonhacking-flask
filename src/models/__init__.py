# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
#
# db_config = {
#     'connection_string': 'sqlite:///car_club.db'
# }
#
# engine = create_engine(db_config['connection_string'], convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
#
# Base = declarative_base()
# Base.query = db_session.query_property()