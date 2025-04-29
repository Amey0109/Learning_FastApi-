from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..database import get_db
from .. import models, schemas
from ..oauth2 import get_current_user

router= APIRouter(
    prefix='/events',
    tags=['ORM_query']
)

@router.get("/", status_code=status.HTTP_200_OK)
def get_event_by_code(Code: str, db: Session= Depends(get_db), current_user:schemas.User = Depends(get_current_user)):
    events= db.query(models.Events).filter(models.Events.Code==Code).first()
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Event of Code {Code} is not available')
    return events


@router.get("/start_date", status_code=status.HTTP_200_OK)
def get_event_by_date(start_date: str, end_date: str, db: Session= Depends(get_db), current_user:schemas.User = Depends(get_current_user)):
    events= db.query(models.Events).filter(models.Events.StartDate==start_date, models.Events.EndDate==end_date).first()
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Event of this date is not available')
    return events
