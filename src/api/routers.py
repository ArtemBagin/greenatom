from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from services import start_robot_from_api, stop_robot_from_api
from schemas import LaunchCreate, LaunchRead

router = APIRouter(
    prefix='/robot',
    tags=['Robot'],
    responses={404: {"description": "Not found"}}
)


@router.post('', response_model=LaunchRead)
async def start_robot(data: LaunchCreate, db: AsyncSession = Depends(get_db)):
    res = await start_robot_from_api(data, db)
    return res


@router.delete('', response_model=LaunchRead)
async def stop_robot(db: AsyncSession = Depends(get_db)):
    res = await stop_robot_from_api(db)
    return res
