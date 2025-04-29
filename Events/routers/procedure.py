from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..database import get_db
from .. import schemas
from ..oauth2 import get_current_user

router= APIRouter()

# Stored Procedure
@router.get('/events/procedure', tags=['Procedure'])
def get_event_by_procedure(code: str, db: Session= Depends(get_db),  current_user:schemas.User = Depends(get_current_user)):
    result= db.execute(
        text(
            'Exec get_event_details @Code=:code'
        ),
        {'code': code}
    )
    events= result.mappings().all()
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Event of this code is not available')
    
    return events