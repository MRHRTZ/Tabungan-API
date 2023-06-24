import structlog
import time
import random
import os
import traceback
import pytz

from dotenv import load_dotenv
from datetime import datetime
from typing import Union, Literal
from .annotations import RandomType, LogLevel

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


def response_message(status: int = 200, remark: str = "", data: str = "", trace_before: int = "") -> dict:
    resp = {
        'trace': get_random(RandomType.INTEGER.value, 15),
        'status': status,
        'remark': remark,
        'result': data
    }

    return resp

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

def setSuccess(data: str, remark: str = "") -> None:
    resp = response_message(200, remark, data)

    return resp


def setFailed(remark: str) -> None:
    resp = response_message(400, remark, "")

    return resp


def setError(remark: str) -> None:
    resp = response_message(500, remark, "")
    generateLog(LogLevel.ERROR, "Error Response", traceback.format_exc(), resp)

    return resp