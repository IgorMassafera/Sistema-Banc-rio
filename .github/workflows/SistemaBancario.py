# Projeto de Sistema Bancário simples utilizando programação orientada a objetos.
# Operações de cadastrar cliente, imprimir o saldo, deposito, saque, e transferencia de uma conta para outra.
# Desenvolvido por Igor Massafera, graduando em Engenharia da Computação pela Universidade Federal de Itajubá - UNIFEI
# 18/05/2024

from cliente import Cliente
from conta import Conta

clientes = []
    
def verificaCPF(cpf): #verifica se já existe um cpf cadastrado
    for c in clientes:
        if c.cliente.cpf == cpf:
            return True
    return False

while(True):
    ans = input('\nO que deseja fazer?\n0- Sair\n1- Cadastrar novo cliente\n2- Saque\n3- Depósito\n4- Transferência\n5- Consultar saldo\n\n')

    if(ans == '0'):
        break

    elif(ans == '1'):
        print('\nObrigado pelo interesse de criar uma conta conosco!\nVamos te fazer algumas perguntas para criar sua nova conta\n')
        nome = input('Qual seu nome? ')
        cpf = input('Por favor nos informe seu CPF no formatato xxx.xxx.xxx-xx: ')
        idade = int(input('Digite sua idade: '))
        if idade >= 18 and verificaCPF(cpf) == False:
            c1 = Cliente(nome, cpf, idade)
            cc1 = Conta(c1)
            clientes.append(cc1)
        elif idade < 18:
            print('\nNão foi possível criar uma conta pois você ainda nao completou 18 anos!\n')
        else:
            print('\nCPF já cadastrado, nao é possivel criar mais de uma conta no mesmo CPF!\n')
    
    elif(ans == '2'):
        n = 0
        cpf = input('\nEntre com seu CPF para prosseguir com o saque: ')
        for customer in clientes:
            if(customer.cliente.cpf == cpf):
                quantia = float(input('Informe o valor desejado para sacar: '))
                customer.saque(quantia)
                break
            else:
                n += 1
        
        if n == len(clientes):
            print('\nCPF nao encontrado, nao foi possivel realizar o saque!')

    elif(ans == '3'):
        n = 0
        cpf = input('\nEntre com seu CPF para prosseguir com o depósito: ')
        for customer in clientes:
            if(customer.cliente.cpf == cpf):
                quantia = float(input('Informe o valor desejado para depositar: '))
                customer.deposito(quantia)
                break
            else:
                n += 1
        
        if n == len(clientes):
            print('\nCPF nao encontrado, nao foi possivel realizar o depósito!')

    elif(ans == '4'):
        n = 0
        cpf = input('\nEntre com seu CPF para prosseguir com a transferência: ')
        for customer in clientes:
            if(customer.cliente.cpf == cpf):
                quantia = float(input('Informe o valor desejado para transferir: '))
                cpf2 = input('\nInforme o CPF do destinatário: ')
                n1 = 0
                for c in clientes:
                    if c.cliente.cpf == cpf2:
                        customer.transferencia(quantia, c)
                        break
                    else:
                        n1 += 1
                if n1 == len(clientes):
                    print('\nCPF de destinatário não encontrado, não foi possível realizar a transferência!')
                break
            else:
                n += 1
        
        if n == len(clientes):
            print('\nCPF não encontrado, não foi possível realizar a transferência!')

    elif(ans == '5'):
        n = 0
        cpf = input('\nEntre com seu CPF para prosseguir com a operação: ')
        for customer in clientes:
            if(customer.cliente.cpf == cpf):
                customer.imprimeSaldo()
                break
            else:
                n += 1
        
        if n == len(clientes):
            print('\nCPF nao encontrado, nao foi possivel consultar o saldo!')

    else:
        print('\nOpção inválida, tente novamente!\n')

print('\nObrigado por confiar em nossos serviços, volte sempre!\n')