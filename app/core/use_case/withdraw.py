
from app.core.entities.nasabah import Withdraw
from app.core.entities.transaction import Transaction, CreateTransaction
from app.adapters.repositories.nasabah_repository import NasabahRepository
from app.adapters.repositories.transaction_repository import TransactionRepository
from app.core.libs.core_utils import get_random, RandomType, getCurrentTime

class WithdrawUseCase:
    def __init__(self):
        self.nasabah_repository = NasabahRepository()
        self.transaction_repository = TransactionRepository()

    def execute(self, user_data: Withdraw) -> dict:
        coreSend = {
            'status': 200,
            'remark': 'Saldo tabungan berhasil ditarik.',
            'result': {}
        }

        count_acc_no = self.nasabah_repository.get_account_no_count(user_data.no_rekening)
        if count_acc_no == 0:
            coreSend['status'] = 400
            coreSend['remark'] = '(999) No Rekening tidak dikenali.'
            return coreSend

        saldo_nasabah = self.nasabah_repository.get_saldo(user_data.no_rekening)
        if count_acc_no == False:
            coreSend['status'] = 400
            coreSend['remark'] = '(999) Gagal mengambil data saldo.'
            return coreSend

        if saldo_nasabah < user_data.nominal:
            coreSend['status'] = 400
            coreSend['remark'] = '(999) Saldo tabungan tidak cukup.'
            return coreSend

        self.nasabah_repository.withdraw(user_data.no_rekening, user_data.nominal)

        amount_now = saldo_nasabah - user_data.nominal

        transactionObj = {}
        transactionObj['account_no'] = user_data.no_rekening
        transactionObj['trx_code'] = 'D'
        transactionObj['amount'] = amount_now
        transactionObj['timestamp'] = getCurrentTime()
        transaction = CreateTransaction(**transactionObj)

        self.transaction_repository.create_transaction(transaction)
        
        coreSend['result'] = {'saldo': amount_now}

        return coreSend