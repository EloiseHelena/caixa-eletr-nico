import random
import string
from tqdm  import tqdm
import time

contas = []

class Banco:
    def __init__(self, titular, senha):
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    #Realizar consulta de saldo
    def consultar(self):
        print(f"Saldo atual: R${self.saldo}")

    #Realizar depósito
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. novo saldo: R$[self.saldo ")

    #Realizar saque
    def sacar(self, valor):
        if self.saldo >= valor:
           self.saldo -= valor
           print(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}")
        else:
           print("Saldo insuficiente.")


    #Realizar tranferencia#
    def transferir(self, valor, outra_conta):
        if self.saldo >= valor:
            outra_conta.saldo += valor
            print()
            print('Atualizando transferência...')
            for _ in tqdm(range(2)):
                time.sleep(1)
            print()
            print(f'Transferência de R${valor} realizada com sucesso para a conta {outra_conta.numero_conta}!')
        else:
            print("Saldo insuficiente para transferência.")

def login():
    while True:
        print('\n ------------  INÍCIO  -------------')
        print('1 - Cadastrar conta')
        print('2 - Entrar na conta')
        print('3 - Sair')
        menu = input('Digite a opção desejada:  ')

        if menu == '1':
            while True:
                cliente = input('Cadastre seu nome: ')
                if cliente.isalpha():
                    break
                else:
                    print('Somente letras!')

            while True:
                codigo = input('Cadastre sua senha: ')
                if codigo.isnumeric():
                    break
                else:
                    print('Somente números!')
            print()
            print(' Criando conta...')
            for _ in tqdm(range(2)):
                time.sleep(1)

            conta = Banco(cliente, codigo)
            conta.numero_conta = random.randint(10000, 99999)
            contas.append(conta)
            print()
            print('  Carregando Sistema...')
            for _ in tqdm(range(2)):
                time.sleep(1)
            print()
            print(f'Sua conta foi criada com sucesso! O número da sua conta é: {conta.numero_conta}.')
            print()
            while True:
                print('\n ------------  MENU  ------------')
                print('1 - Consultar Saldo')
                print('2 - Depositar')
                print('3 - Sacar')
                print('4 - Transferir')
                print('5 - Sair')
                opcao = input('Digite a opção desejada: ')

                if opcao == '1':
                    conta.consultar()
                elif opcao == '2':
                    valor = float(input('Digite valor a ser depositado: R$'))
                    conta.depositar(valor)
                elif opcao == '3':
                    valor = float(input('Digite o valor a ser sacado: R$'))
                    conta.sacar(valor)
                elif opcao == '4':
                    valor = float(input('Digite o valor a ser transferido: R$'))
                    nome = input('Digite o nome do titular que receberá a transferência: ')
                    if nome.lower() == conta.titular.lower():
                        print('Não é possível transferir para a própria conta.')
                    else:
                        encontrou_conta = False
                        for c in contas:
                            if c.titular.lower() == nome.lower():
                                outra_conta = c
                                encontrou_conta = True
                                break
                        if encontrou_conta:
                            conta.transferir(valor, outra_conta)
                        else:
                            print('Titular da conta não encontrado.')
                elif opcao == '5':
                    print()
                    print('Você saiu do programa...  \n')
                    return
                else:
                    print('Opção inválida!')
        elif menu == '2':
            nome = input('Digite seu nome: ')
            for conta in contas:
                if nome == conta.titular:
                    senha = input('Digite sua senha: ')
                    if senha == conta.senha:
                        print(f'Bem-vindo de volta, {nome}!')
                        return
                    else:
                        print('Senha incorreta.')
                        break
            else:
                print('Conta não encontrada.')
        elif menu == '3':
            print('Você saiu do programa...  \n')
            quit()
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    login()








