import datetime
import subprocess
import psutil
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import LaunchCreate
from models import Launch
from config import settings


def get_bot() -> psutil.Process | None:
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == 'python.exe':
            cmdline = process.cmdline()
            if len(cmdline) > 1 and cmdline[1].endswith(settings.robot_file_name):
                return process


def bot_is_run() -> bool:
    """
    :return:
        bool: True, if script is running, else False.
    """
    return bool(get_bot())


def stop_bot():
    process = get_bot()
    process.terminate()


def run_bot(start_num: int):
    if not bot_is_run():
        subprocess.Popen(["python", settings.robot_path, "--start", str(start_num)])


async def start_robot_from_api(data: LaunchCreate, db: AsyncSession):
    if bot_is_run():
        raise HTTPException(
            status_code=400,
            detail="Robot already start",
        )
    new_launch = Launch(start_num=data.start_num)
    db.add(new_launch)
    await db.commit()
    await db.refresh(new_launch)
    run_bot(start_num=data.start_num)
    return new_launch


async def stop_robot_from_api(db: AsyncSession):
    if not bot_is_run():
        raise HTTPException(
            status_code=400,
            detail="Robot already stop",
        )
    stmt = select(Launch).order_by(-Launch.id)
    last_launch = await db.execute(stmt)
    last_launch = last_launch.scalars().first()
    last_launch.end_at = datetime.datetime.now()
    work_time = (last_launch.end_at - last_launch.start_at).total_seconds()
    last_launch.work_time = int(work_time)
    db.add(last_launch)
    await db.commit()
    stop_bot()
    return last_launch
