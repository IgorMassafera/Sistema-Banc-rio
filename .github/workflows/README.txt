Desenvolvido por Igor Massafera 
Graduando em Engenharia de Computação 
UNIVERSIDADE FEDERAL DE ITAJUBÁ - UNIFEI
18/05/2024

O seguinte projeto conta com 3 arquivos python: cliente.py, conta.py e SistemaBancario.py

No arquivo cliente.py está a declaração da classe Cliente, seus atributos são nome(string), cpf(string) e idade(inteiro)

No arquivo conta.py está a declaração da classe Conta, seus atributos sao cliente(Objeto Cliente), numero(string) e saldo(float)

A classe Conta implementa métodos para consultar saldo da conta, realizar saque, depósito, e transferência de uma conta para outra

O arquivo SistemaBancario.py conta com um menu recursivo para aplicação dos métodos citados, onde o usuário deve digitar:

0 - Sair 
1 - Cadastrar nova conta
2 - Saque 
3 - Depósito 
4 - Transferência 
5 - Consultar saldo

OBS: não é possível cadastrar mais de uma conta no mesmo CPF e a idade deve ser maior ou igual a 18 anos.