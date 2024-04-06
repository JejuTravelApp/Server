from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from models.datebase import Base

class PlanBase(BaseModel):
    ptitle: str
    pmemo: Optional[str] = None
    prating: Optional[float] = None
    gid: int
    pcompletestatus: int = 0

class PlanCreate(PlanBase):
    pass

class Plan(PlanBase):
    pid: int

    class Config:
        orm_mode = True

class PlangroupBase(BaseModel):
    gtitle: str
    gfriend: Optional[str] = None
    gcolor: int
    gcompletestatus: int
    gstartdate: date
    genddate: date

class PlangroupCreate(PlangroupBase):
    pass

class Plangroup(PlangroupBase):
    gid: int
    plans: List[Plan] = []

    class Config:
        orm_mode = True

class HeartmarkerBase(BaseModel):
    hmname: str
    hmlatitude: float
    hmlongitude: float

class HeartmarkerCreate(HeartmarkerBase):
    pass

class Heartmarker(HeartmarkerBase):
    hmid: int

    class Config:
        orm_mode = True

class MapmarkerBase(BaseModel):
    mname: str
    mlatitude: float
    mlongitude: float

class MapmarkerCreate(MapmarkerBase):
    pass

class Mapmarker(MapmarkerBase):
    mpid: int

    class Config:
        orm_mode = True

class RecordBase(BaseModel):
    rtitle: str
    rtag: str
    rphoto: str
    rreview: str
    rfirend: Optional[str] = None
    rstartdate: date
    renddate: date

class RecordCreate(RecordBase):
    pass

class Record(RecordBase):
    rid: int

    class Config:
        orm_mode = True

class PlanMarkingBase(BaseModel):
    ppid: int
    pmid: int
    pmname: str
    pmlatitude: float
    pmlongitude: float

class PlanMarkingCreate(PlanMarkingBase):
    pass

class PlanMarking(PlanMarkingBase):
    class Config:
        orm_mode = True

class RecordMarkingBase(BaseModel):
    rmid: int
    rrid: int
    rmname: str
    rmlatitude: float
    rmlongitude: float

class RecordMarkingCreate(RecordMarkingBase):
    pass

class RecordMarking(RecordMarkingBase):
    class Config:
        orm_mode = True

class RecordingBase(BaseModel):
    rgid: int
    rpid: int

class RecordingCreate(RecordingBase):
    pass

class Recording(RecordingBase):
    class Config:
        orm_mode = True

class SearchBase(BaseModel):
    searchname: str
    searchdate: date

class SearchCreate(SearchBase):
    pass

class Search(SearchBase):
    sid: int

    class Config:
        orm_mode = True
