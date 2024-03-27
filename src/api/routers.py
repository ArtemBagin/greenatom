from fastapi import APIRouter

from src.api.schemas import StartScheme

router = APIRouter(
    prefix='/robot',
    tags=['Robot'],
    responses={404: {"description": "Not found"}}
)


@router.post('')
def start_robot(data: StartScheme):
    # todo: вызов функции из services
    ...


@router.delete('')
def start_robot(data: StartScheme):
    # todo: вызов функции из services
    ...
