from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..database import get_db
from datetime import date
from ..import schemas, oauth2

router= APIRouter(
    prefix= '/events',
    tags=['Normal_Query']
)

# Using normal query
@router.get("/code", status_code=status.HTTP_200_OK)
def get_event_by_code(code: str, db: Session= Depends(get_db),  current_user:schemas.User = Depends(oauth2.get_current_user)):
    result= db.execute(
        text('''Select e.Id, EventName, e.Code, StartDate,EndDate, OfficeName, RegionName 
            from Events e inner join Offices_LKUP o on e.OfficeId=o.Id 
            inner join Regions_LKUP r on e.RegionId=r.Id
             where e.Code= :code'''),
            {'code': code}
        )
    events= result.mappings().all()
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Event of this code is not available')
    return events

@router.get("/date", status_code=status.HTTP_200_OK)
def get_event_by_date(start_date: date, end_date: date, db: Session= Depends(get_db),  current_user:schemas.User = Depends(oauth2.get_current_user)):
    result= db.execute(
        text('Select * from Events where cast(StartDate as date)= :start_date and cast(EndDate as date)= :end_date'),
        {'start_date': start_date, 'end_date': end_date}
    )
    events= result.mappings().all()
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Event of this date is not available')
    return events
