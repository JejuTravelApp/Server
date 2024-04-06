from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.datebase import Base

class Plan(Base):
    __tablename__ = 'plan'
    pid = Column(Integer, primary_key=True)
    ptitle = Column(String(20), nullable=False)
    pmemo = Column(Text)
    prating = Column(Float)
    pgid = Column(Integer, ForeignKey('plangroup.gid'), nullable=False)
    pcompletestatus = Column(Integer, nullable=False, default=0)

class Plangroup(Base):
    __tablename__ = 'plangroup'
    gid = Column(Integer, primary_key=True)
    gtitle = Column(String(20), nullable=False)
    gfriend = Column(String(100))
    gcolor = Column(Integer, nullable=False)
    gcompletestatus = Column(Integer, nullable=False)
    gstartdate = Column(Date, nullable=False)
    genddate = Column(Date, nullable=False)

    plans = relationship("Plan", backref="plangroup")

class Heartmarker(Base):
    __tablename__ = 'heartmarker'
    hmid = Column(Integer, primary_key=True)
    hmname = Column(String(10), nullable=False)
    hmlatitude = Column(Float, nullable=False)
    hmlongitude = Column(Float, nullable=False)

class Mapmarker(Base):
    __tablename__ = 'mapmarker'
    mpid = Column(Integer, primary_key=True)
    mname = Column(String(10), nullable=False)
    mlatitude = Column(Float, nullable=False)
    mlongitude = Column(Float, nullable=False)

class Record(Base):
    __tablename__ = 'record'
    rid = Column(Integer, primary_key=True)
    rtitle = Column(String(45), nullable=False)
    rtag = Column(Text, nullable=False)
    rphoto = Column(Text, nullable=False)
    rreview = Column(Text, nullable=False)
    rfirend = Column(String(100))
    rstartdate = Column(Date, nullable=False)
    renddate = Column(Date, nullable=False)

class PlanMarking(Base):
    __tablename__ = 'plan_marking'
    ppid = Column(Integer, ForeignKey('plan.pid'), primary_key=True)
    pmid = Column(Integer, ForeignKey('mapmarker.mpid'), primary_key=True)
    pmname = Column(String(10), nullable=False)
    pmlatitude = Column(Float, nullable=False)
    pmlongitude = Column(Float, nullable=False)

class RecordMarking(Base):
    __tablename__ = 'record_marking'
    rmid = Column(Integer, ForeignKey('mapmarker.mpid'), primary_key=True)
    rrid = Column(Integer, ForeignKey('record.rid'), primary_key=True)
    rmname = Column(String(10), nullable=False)
    rmlatitude = Column(Float, nullable=False)
    rmlongitude = Column(Float, nullable=False)

class Recording(Base):
    __tablename__ = 'recording'
    rgid = Column(Integer, ForeignKey('plangroup.gid'), primary_key=True)
    rpid = Column(Integer, ForeignKey('record.rid'), primary_key=True)

class Search(Base):
    __tablename__ = 'search'
    sid = Column(Integer, primary_key=True)
    searchname = Column(String(45), nullable=False)
    searchdate = Column(Date, nullable=False)
