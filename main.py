from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente("Matheus", 19)
cliente2 = Cliente("Elaine", 50)
cliente3 = Cliente("Eduardo", 20)
cliente4 = Cliente("Fernanda", 26)
cliente5 = Cliente("Aluísio", 35)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaPoupanca(2222, 254336, 0)
conta3 = ContaPoupanca(1231, 254456, 0)
conta4 = ContaCorrente(3333, 321312, 0)
conta5 = ContaCorrente(1526, 321312, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)
cliente4.inserir_conta(conta4)
cliente5.inserir_conta(conta5)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

banco.inserir_cliente(cliente4)
banco.inserir_conta(conta4)

banco.inserir_cliente(cliente5)
banco.inserir_conta(conta5)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(100)
    cliente1.conta.sacar(100)
else:
    print("Cliente não autenticado")

if banco.autenticar(cliente4):
    cliente4.conta.sacar(100)
else:
    print("Cliente não autenticado")

if banco.autenticar(cliente5):
    cliente5.conta.sacar(100)
else:
    print("Cliente não autenticado")
