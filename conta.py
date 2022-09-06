from abc import abstractmethod, ABC


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Foi depositado R$ {valor:.2f}")
        self.detalhes()
        print()

    def detalhes(self):
        print(f"Agencia: {self.agencia} "
              f"Conta: {self.conta}"
              f" Saldo: R$ {self.saldo:.2f}")

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
        print(f"Foi sacado R$ {valor:.2f} da sua conta")
        self.detalhes()
        print()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo Insuficiente")
            return

        self.saldo -= valor
        print(f"Foi sacado R$ {valor:.2f} da sua conta")
        self.detalhes()
        print()
