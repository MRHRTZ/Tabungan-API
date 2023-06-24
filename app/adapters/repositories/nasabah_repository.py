import sys, traceback

from . import engine
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.entities.nasabah import CreateNasabah, Nasabah
from app.adapters.utils import generateLog, LogLevel
from app.adapters.utils import querying as query_util


class NasabahRepository:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.table_name = "nasabah"

    def get_next_account_no(self):
        account_no = ""
        try:
            sSQL = "SELECT nextval('seq_account_no') as account_no"
            account_no = self.session.execute(text(sSQL)).first()._asdict().get('account_no')

            self.session.commit()
            return account_no
        except Exception as e:
            self.session.rollback()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def create_nasabah(self, nasabah: Nasabah):
        try:
            sSQL, values = query_util.generate_insert_sql_from_model(self.table_name, nasabah)
            sSQL = sSQL % values

            self.session.execute(text(sSQL))

            self.session.commit()
            self.session.close()

        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def get_phone_count(self, phone: str):
        try:
            sSQL = "select count(*) from {0} n where n.phone = {1!r}".format(self.table_name, phone)
            count = self.session.execute(text(sSQL)).first()._asdict().get('count')
            count = int(count)

            self.session.commit()
            self.session.close()

            return count
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def get_nik_count(self, nik: str):
        try:
            sSQL = "select count(*) from {0} n where n.nik = {1!r}".format(self.table_name, nik)
            count = self.session.execute(text(sSQL)).first()._asdict().get('count')
            count = int(count)

            self.session.commit()
            self.session.close()

            return count
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def get_account_no_count(self, account_no: str):
        try:
            sSQL = "select count(*) from {0} n where n.account_no = {1!r}".format(self.table_name, account_no)
            count = self.session.execute(text(sSQL)).first()._asdict().get('count')
            count = int(count)

            self.session.commit()
            self.session.close()

            return count
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def get_nasabah(self, account_no: str):
        try:
            sSQL = "select * from {0} n where n.account_no = {1!r}".format(self.table_name, account_no)
            result = self.session.execute(text(sSQL)).first()._asdict()

            self.session.commit()
            self.session.close()

            return result
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False
    
    def get_saldo(self, account_no: str):
        try:
            sSQL = "select balance from {0} n where n.account_no = {1!r}".format(self.table_name, account_no)
            saldo = self.session.execute(text(sSQL)).first()._asdict().get('balance')
            saldo = int(saldo)

            self.session.commit()
            self.session.close()

            return saldo
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def save_money(self, account_no: str, amount: int):
        try:
            condition = "account_no = {0!r}".format(account_no)
            sSQL, values = query_util.generate_update_sql(self.table_name, {'balance': 'balance+' + str(amount)}, condition)
            sSQL = sSQL % values

            self.session.execute(text(sSQL))

            self.session.commit()
            self.session.close()
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def withdraw(self, account_no: str, amount: int):
        try:
            condition = "account_no = {0!r}".format(account_no)
            sSQL, values = query_util.generate_update_sql(self.table_name, {'balance': 'balance-' + str(amount)}, condition)
            sSQL = sSQL % values

            self.session.execute(text(sSQL))

            self.session.commit()
            self.session.close()
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False