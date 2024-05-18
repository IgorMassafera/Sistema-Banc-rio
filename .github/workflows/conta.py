from random import randint

class Conta:
    def __init__(self, cliente, numero = [], saldo = 0):

        numero = []

        for i in range(0,9):
            numero.append(str(randint(0,9)))

        numero.append('-')
        numero.append(str(randint(0,9)))
        numero = ''.join(numero)

        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo

        print('\nConta criada com sucesso!\nNúmero da conta:',self.numero,'\nSaldo inicial:',self.saldo)

    def imprimeSaldo(self):
        print(self.cliente.nome, 'o seu saldo é de' , self.saldo)

    def deposito(self, quantia):
        self.saldo += quantia
        print('Depósito de', quantia, 'realizado com sucesso!')

    def saque(self, quantia):
        if self.saldo >= quantia:
            self.saldo -= quantia
            print(self.cliente.nome, 'seu saque de', quantia, 'foi realizado com sucesso! ')
        else:
            print(self.cliente.nome, 'você nao tem saldo suficiente para realizar o saque!')

    def transferencia(self, quantia, c2):
        if self.saldo >= quantia:
            c2.saldo += quantia
            self.saldo -= quantia
            print('Transferência de', quantia, 'para', c2.cliente.nome, 'feita com sucesso!')
        else:
            print('Você nao tem saldo suficiente para realizar a transferência para', c2.cliente.nome)