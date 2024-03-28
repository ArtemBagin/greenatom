from fastapi import APIRouter

from src.api.schemas import LaunchCreate

router = APIRouter(
    prefix='/robot',
    tags=['Robot'],
    responses={404: {"description": "Not found"}}
)


@router.post('')
def start_robot(data: LaunchCreate):
    # todo: вызов функции из services
    ...


@router.delete('')
def start_robot(data: LaunchCreate):
    # todo: вызов функции из services
    ...
