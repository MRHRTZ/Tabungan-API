import structlog
import sys

from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.adapters.utils import setSuccess, setError, setFailed
from app.core.entities.nasabah import CreateNasabah, SaveMoney, Withdraw, Mutation
from app.adapters.controllers.nasabah_controller import NasabahController
from app.adapters.utils import generateLog, LogLevel

router = APIRouter()
log = structlog.get_logger('uvicorn')


@router.post("/daftar", description="Pendaftaran Nasabah")
async def Register_User(request: CreateNasabah):
    response = setSuccess("", "Berhasil mendaftarkan nasabah!")
    try:
        if request.nama in [None, "", 0]:
            response = setFailed('field nama masih kosong!')
        elif request.nik in [None, "", 0]:
            response = setFailed('field nik masih kosong!')
        elif request.no_hp in [None, "", 0]:
            response = setFailed('field no_hp masih kosong!')

        if response['status'] == 200:
            nasabahConn = NasabahController()
            coreResp = nasabahConn.create_user(request)

            response['status'] = coreResp['status']
            response['remark'] = coreResp['remark']
            response['result'] = coreResp['result']
        
            generateLog(LogLevel.INFO, "Success Response", "", response)
        else:
            generateLog(LogLevel.WARNING, "Failed Response", response['remark'], response)
    except Exception as e:
        response = setError("(99) Gagal mendaftar!")
    # --

    return response
# --

@router.post("/tabung", description="Tabung saldo nasabah")
async def Save_Money(request: SaveMoney):
    response = setSuccess("", "Berhasil menambah saldo tabungan!")
    try:
        if request.no_rekening in [None, "", 0]:
            response = setFailed('field no_rekening masih kosong!')
        elif request.nominal in [None, "", 0]:
            response = setFailed('field nominal masih kosong!')
        if response['status'] == 200:
            nasabahConn = NasabahController()
            coreResp = nasabahConn.save_money(request)

            response['status'] = coreResp['status']
            response['remark'] = coreResp['remark']
            response['result'] = coreResp['result']
        
            generateLog(LogLevel.INFO, "Success Response", "", response)
        else:
            generateLog(LogLevel.WARNING, "Failed Response", response['remark'], response)
    except Exception as e:
        response = setError("(99) Gagal menambah tabungan!")
    # --

    return response
# --


@router.post("/tarik", description="Tarik saldo nasabah")
async def Withdraw(request: Withdraw):
    response = setSuccess("", "Berhasil menarik saldo!")
    try:
        if request.no_rekening in [None, "", 0]:
            response = setFailed('field no_rekening masih kosong!')
        elif request.nominal in [None, "", 0]:
            response = setFailed('field nominal masih kosong!')
        if response['status'] == 200:
            nasabahConn = NasabahController()
            coreResp = nasabahConn.withdraw(request)

            response['status'] = coreResp['status']
            response['remark'] = coreResp['remark']
            response['result'] = coreResp['result']
        
            generateLog(LogLevel.INFO, "Success Response", "", response)
        else:
            generateLog(LogLevel.WARNING, "Failed Response", response['remark'], response)
    except Exception as e:
        response = setError("(99) Gagal menarik saldo!")
    # --

    return response
# --


@router.post("/mutasi", description="Mutasi nasabah")
async def Mutation(request: Mutation):
    response = setSuccess("", "Berhasil mengambil data mutasi!")
    try:
        if request.no_rekening in [None, "", 0]:
            response = setFailed('field no_rekening masih kosong!')

        if response['status'] == 200:
            nasabahConn = NasabahController()
            coreResp = nasabahConn.get_mutation(request)

            response['status'] = coreResp['status']
            response['remark'] = coreResp['remark']
            response['result'] = coreResp['result']
        
            generateLog(LogLevel.INFO, "Success Response", "", response)
        else:
            generateLog(LogLevel.WARNING, "Failed Response", response['remark'], response)
    except Exception as e:
        response = setError("(99) Gagal menarik saldo!")
    # --

    return response
# --
