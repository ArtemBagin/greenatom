import subprocess
import psutil

from src.api.config import settings


def get_bot() -> psutil.Process | None:
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == 'python.exe':
            cmdline = process.cmdline()
            if len(cmdline) > 1 and cmdline[1].endswith(settings.robot_file_name):
                return process


def get_status() -> bool:
    """
    :return:
        bool: True, if script is running, else False.
    """
    return bool(get_bot())


def stop_bot():
    process = get_bot()
    assert process, "Process not found"
    process.terminate()


def run_bot(start_num: int):
    if not get_status():
        subprocess.Popen(["python", settings.robot_path, "--start", str(start_num)])
