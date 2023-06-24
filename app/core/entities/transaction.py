from pydantic import BaseModel
from typing import Optional

class CreateTransaction(BaseModel):
    account_no: Optional[str]
    trx_code: Optional[str]
    amount: Optional[int]
    timestamp: Optional[str]

class ResponseMutation(BaseModel):
    waktu: Optional[str]
    kode_transaksi: Optional[str]
    nominal: Optional[int]

class Transaction(BaseModel):
    transaction_id: Optional[int]
    account_no: Optional[str]
    trx_code: Optional[str]
    amount: Optional[int]
    timestamp: Optional[str]