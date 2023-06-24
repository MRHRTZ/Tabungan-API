import sys, traceback

from . import engine
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.entities.transaction import Transaction, ResponseMutation
from app.adapters.utils import generateLog, LogLevel
from app.adapters.utils import querying as query_util


class TransactionRepository:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.table_name = "transactions"

    def create_transaction(self, transaction: Transaction):
        try:
            sSQL, values = query_util.generate_insert_sql_from_model(self.table_name, transaction)
            sSQL = sSQL % values

            generateLog(LogLevel.DEBUG, "Create Trx", sSQL)

            self.session.execute(text(sSQL))

            self.session.commit()
            self.session.close()

        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False

    def get_transaction(self, account_no: str):
        try:
            sSQL = "select * from {0} n where n.account_no = {1!r}".format(self.table_name, account_no)
            result = self.session.execute(text(sSQL)).all()
            result = [ResponseMutation(waktu=time.strftime('%Y-%m-%d %H:%M:%S'), kode_transaksi=trx_code, nominal=amount) for id, acc_no, trx_code, amount, time in result]

            self.session.commit()
            self.session.close()

            return result
        except Exception as e:
            self.session.rollback()
            self.session.close()
            generateLog(LogLevel.ERROR, "Repo Error", traceback.format_exc())

            return False