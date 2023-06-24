import structlog
import time
import random
import os
import traceback
import pytz

from dotenv import load_dotenv
from datetime import datetime
from typing import Union, Literal
from . import RandomType, LogLevel

load_dotenv()

log = structlog.get_logger('uvicorn')

def get_random(random_type: Literal[RandomType.STRING, RandomType.INTEGER] = RandomType.INTEGER, length: int = 3) -> str:
    if random_type == RandomType.STRING:
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits)
                             for i in range(length)))
    else:
        range_start = 10**(length-1)
        range_end = (10**length)-1
        result_str = str(random.randint(range_start, range_end))

    return result_str

def generateLog(
    logLevel:  Literal[LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR, LogLevel.CRITICAL], 
    title: str,
    msg: str = "",
    data: any = "",
):
    title = title if title else '-'
    strGen = "\n"
    strGen += "="*10 + f"[ {title} ]" + "="*10+"\n"
    strGen += "Message : " + (str(msg) if msg else '-')+"\n"
    strGen += "Response : " + (str(data) if data else '-')+"\n"
    strGen += "="*(24+len(title))
    
    if logLevel == LogLevel.DEBUG:
        log.debug(strGen)
    elif logLevel == LogLevel.INFO:
        log.info(strGen)
    elif logLevel == LogLevel.WARNING:
        log.warn(strGen)
    elif logLevel == LogLevel.ERROR:
        log.error(strGen)
    elif logLevel == LogLevel.CRITICAL:
        log.critical(strGen)

def getCurrentTime(format: str = '%Y-%m-%d %H:%M:%S') -> str:
    current_datetime = datetime.now()
    tz = os.environ.get('TIMEZONE')
    generateLog(LogLevel.DEBUG, "test date", tz)
    timezone = pytz.timezone(tz)
    current_datetime_wib = current_datetime.astimezone(timezone)
    formatted_time = current_datetime_wib.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_time