from app.core.entities.nasabah import CreateNasabah, Nasabah
from app.adapters.repositories.nasabah_repository import NasabahRepository
from app.adapters.utils import get_random, RandomType

class CreateNasabahUseCase:
    def __init__(self):
        self.nasabah_repository = NasabahRepository()

    def execute(self, user_data: CreateNasabah) -> dict:
        coreSend = {
            'status': 200,
            'remark': 'Pendaftaran berhasil',
            'result': {}
        }

        count_nik = self.nasabah_repository.get_nik_count(user_data.nik)
        if count_nik != 0:
            coreSend['status'] = 400
            coreSend['remark'] = '(999) NIK telah terdaftar.'
            return coreSend

        count_phone = self.nasabah_repository.get_phone_count(user_data.no_hp)
        if count_phone != 0:
            coreSend['status'] = 400
            coreSend['remark'] = '(999) No Hp telah terdaftar.'
            return coreSend

        next_acc_no = self.nasabah_repository.get_next_account_no()
        if not next_acc_no:
            coreSend['status'] = 400
            coreSend['remark'] = '(999) Gagal mendapatkan no rekening.'
            return coreSend

        account_no = int(get_random(RandomType.INTEGER, 5)) + int(next_acc_no)
        account_no = get_random(RandomType.INTEGER, 4) + str(account_no).zfill(10)

        newNasabah = {}
        newNasabah['account_no'] = account_no
        newNasabah['full_name'] = user_data.nama.upper()
        newNasabah['nik'] = user_data.nik
        newNasabah['phone'] = user_data.no_hp

        nasabah = Nasabah(**newNasabah)
        self.nasabah_repository.create_nasabah(nasabah)

        coreSend['result'] = {'account_no': account_no}

        return coreSend