from datetime import datetime
from time import time

from pydantic import BaseModel


class LaunchCreate(BaseModel):
    start_num: int = 0


class LaunchRead(LaunchCreate):
    id: int
    start_at: datetime
    end_at: datetime | None
    work_time: int | None
