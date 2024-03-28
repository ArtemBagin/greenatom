from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from services import start_robot_from_api, stop_robot_from_api, get_all_launches, get_launch_by_pk
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


@router.get('', response_model=list[LaunchRead])
async def launches(db: AsyncSession = Depends(get_db)):
    res = await get_all_launches(db)
    return res


@router.get('/{pk}', response_model=LaunchRead)
async def launch_by_pk(pk: int, db: AsyncSession = Depends(get_db)):
    res = await get_launch_by_pk(pk, db)
    return res
