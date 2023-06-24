import os
import sys
import structlog

from app.core.use_case.create_nasabah import CreateNasabahUseCase
from app.core.use_case.save_money import SaveMoneyUseCase
from app.core.use_case.withdraw import WithdrawUseCase
from app.core.use_case.mutation import MutationUseCase
from  app.core.entities.nasabah import CreateNasabah, SaveMoney, Withdraw, Mutation

log = structlog.get_logger('uvicorn')

class NasabahController:
    def __init__(self):
        self.create_nasabah_use_case = CreateNasabahUseCase()
        self.save_money_use_case = SaveMoneyUseCase()
        self.withdraw_use_case = WithdrawUseCase()
        self.mutation_use_case = MutationUseCase()

    def create_user(self, user_data: CreateNasabah):
        result = self.create_nasabah_use_case.execute(user_data)
        return result

    def save_money(self, request_data: SaveMoney):
        result = self.save_money_use_case.execute(request_data)
        return result

    def withdraw(self, request_data: Withdraw):
        result = self.withdraw_use_case.execute(request_data)
        return result

    def get_mutation(self, request_data: Mutation):
        result = self.mutation_use_case.execute(request_data)
        return result
