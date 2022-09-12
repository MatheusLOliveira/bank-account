from abc import abstractmethod, ABC
from data import FORMATACAO
from log import log


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        log(self.conta, 'depósito', FORMATACAO, valor)
        print(f"Valor depositado: R${valor:.2f}\n"
              f"Solicitado em: {FORMATACAO}".replace('.', ','))
        self.detalhes()
        print()

    def detalhes(self):
        print(f"Agencia: {self.agencia} "
              f"Conta: {self.conta}"
              f" Saldo: R$ {self.saldo:.2f}".replace('.', ','))

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo Insuficiente")
            return

        self.saldo -= valor
        log(self.conta, 'saque', FORMATACAO, valor)
        print(f"Valor do saque: R${valor:.2f}\n"
              f"Solicitado em: {FORMATACAO}".replace('.', ','))
        self.detalhes()
        print()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo Insuficiente")
            return

        self.saldo -= valor
        log(self.conta, 'saque', FORMATACAO, valor)
        print(f"Valor do saque: R${valor:.2f}\n"
              f"Solicitado em: {FORMATACAO}".replace('.', ','))
        self.detalhes()
        print()
