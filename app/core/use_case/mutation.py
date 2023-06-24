
from app.core.entities.nasabah import Mutation
from app.core.entities.transaction import Transaction, CreateTransaction
from app.adapters.repositories.nasabah_repository import NasabahRepository
from app.adapters.repositories.transaction_repository import TransactionRepository
from app.core.libs.core_utils import get_random, RandomType, getCurrentTime

class MutationUseCase:
    def __init__(self):
        self.nasabah_repository = NasabahRepository()
        self.transaction_repository = TransactionRepository()

    def execute(self, user_data: Mutation) -> dict:
        coreSend = {
            'status': 200,
            'remark': 'Berhasil mengambil data mutasi.',
            'result': {}
        }

        count_acc_no = self.nasabah_repository.get_account_no_count(user_data.no_rekening)
        if count_acc_no == 0:
            coreSend['status'] = 400
            coreSend['remark'] = '(999) No Rekening tidak dikenali.'
            return coreSend

        mutation_data = self.transaction_repository.get_transaction(user_data.no_rekening)
        
        coreSend['result'] = {'mutasi': mutation_data}

        return coreSend