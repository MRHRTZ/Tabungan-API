from pydantic import BaseModel
from typing import Optional

class CreateNasabah(BaseModel):
    nama: Optional[str]
    nik: Optional[str]
    no_hp: Optional[str]

class SaveMoney(BaseModel):
    no_rekening: Optional[str]
    nominal: Optional[int]

class Withdraw(BaseModel):
    no_rekening: Optional[str]
    nominal: Optional[int]

class Mutation(BaseModel):
    no_rekening: Optional[str]

class Nasabah(BaseModel):
    account_no: Optional[str]
    full_name: Optional[str]
    nik: Optional[str]
    phone: Optional[str]
    balance:  Optional[int] = 0