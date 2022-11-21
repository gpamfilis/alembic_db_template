from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)

    # id
    # Full name
    # ynab api key
    # wise api key

class Flow(Base):
    __tablename__ = 'flow'
    id = Column(Integer, primary_key=True, index=True)

    # id
    # name
    # Description
    # start_date
    # end_date
    # type [recuring, oneoff]
    # use: [Personal, Buziness]
    # direction [inflow, outflow]
    pass

class FlowTransaction(Base):
    __tablename__ = 'flow_transaction'

    id = Column(Integer, primary_key=True, index=True)

    # id
    # name
    # Description
    # start_date
    # end_date
    # type [recuring, oneoff]
    # use: [Personal, Buziness]
    # current amount
    # tags 



