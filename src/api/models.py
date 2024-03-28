from datetime import datetime, UTC

from sqlalchemy import TIMESTAMP, Integer
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Launch(Base):
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    start_num: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    start_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    end_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True, default=None)
    work_time: Mapped[int] = mapped_column(Integer, nullable=True, default=None)
