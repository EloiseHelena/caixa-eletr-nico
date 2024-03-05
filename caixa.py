import random
import string
from tqmd  import tqmd
import time

class caixa:
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
         
         