from data_storage import DataStorage
from tkinter import *
from tkinter import messagebox


ds = DataStorage()


print('Seja bem-vindo ao gerenciador de inscritos para o evento!')
while True:
    print('O que gostaria de fazer? (Escolha uma opção)')
    print('1 - Cadastrar Novo Usuário')
    print('2 - Listar usuários ordenados por data de cadastro')
    print('3 - Listar usuários por ordem alfaética')
    print('4 - Buscar usuário')
    print('7 - Sair')

    opcao = int(input())
    
    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 7:
        break


print('Obrigado por usar nosso gerenciador de exentos!')
print('Até a Próxim!!!')
