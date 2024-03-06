import random
import string
from tqdm  import tqdm
import time

class banco:
 def __init__(self, titular, codigo):
     self.titular: titular
     self.numero_conta = ''.join(random.choices(string.digits, k=5))
     self.saldo = 0
     self.codigo = codigo


 def depositar(self, valor):
        self.saldo += valor
        print()
        print('Atualizando depósito...')
        for i in tqdm(range(2)):
           time.sleep
        print()
        print(f'Depósito realizado com sucesso! Novo saldo: R${self.saldo:.2f}')

 def sacar(self, valor):
     if valor > self.saldo:
         print()
         print('Atualizando saque...')
         for i in tqdm(range(2)):
             time.sleep(1)
         print()
         print('Saldo insuficiente.')
     else:
         self.saldo -= valor
         print()
         print('Atualizando saque...')
         for i in tqdm(range(2)):
             time.sleep(1)
         print()
         print(f'Saque realizado com sucesso! Novo saldo: R${self.saldo:.2f}')
         
 def consultar(self):
         print()
         print('Atualizando saldo...')
         for i in tqdm(range(2)):
             time.sleep(1)
         print()
         print(f'Titular: {self.titular}')
         print(f'Número da conta: {self.numero_conta}')
         print(f'Saldo: R${self.saldo:.2f}')
     
 def transferir(self, valor, numero_conta):
        if valor > self.saldo:
         print()
         print('Atualizando tranferência...')
         for i in tqdm(range(2)):
             time.sleep(1)
         print()
        else:
            self.saldo -= valor
            numero_conta.saldo += valor
            print()
            print('Atualizando transferência...')
        for i in tqdm(range(2)):
             time.sleep(1)
             print()
             print(f'Transferência realizada com sucesso para a conta {conta.numero_conta}!')
        while True:
            usuario = input('Cadastre seu nome: ')
            if all(c.isalpha() for c in usuario):
                break
            else:
                print('Somente letras!')

        while True:
            senha = input('Cadastre sua senha: ')
            if all (c.isnumeric() for c in senha):
                break
            else:
                print('Somente números!')
            print()
            print('Criando conta...')
            for i in tqdm(range(2)):
                time.sleep(1)
        
        nome = input('Digite seu nome: ')
        while nome != usuario:
            nome = input('Nome incorreto! Digite novamente: ')
        validar = input('Digite sua senha: ')
        while validar != senha:
            validar = input('Senha incorreta! Digite novamente: ')
        else:
            print(f'Bem vindo(a) {usuario}')

        conta = banco(usuario, senha)
        conta.numero_conta = random.randint(10000, 99999)
            print()
            print(f'Sua conta foi criada com sucesso! Seu número de conta é: {conta.numero_conta}.')
            print()

            contas = []
            
             
         
            
    