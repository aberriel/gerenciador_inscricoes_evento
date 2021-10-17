from data_storage import DataStorage


ds = DataStorage()


print('Seja bem-vindo ao gerenciador de inscritos para o evento!')
while True:
    print('O que gostaria de fazer? (Escolha uma opção)')
    print('1 - Cadastrar Novo Usuário')
    print('2 - Listar usuários ordenados por data de cadastro')
    print('3 - Listar usuários por ordem alfaética')
    print('4 - Buscar usuário')
    print('5 - Remover usuário')
    print('6 - Alterar nome de usuário')
    print('7 - Sair')

    opcao = int(input())
    
    if opcao == 1:
        first_name = input('Qual o primeiro nome do usuário?')
        last_name = input('qual o último nome da pessoa?')
        email = input('Qual o endereço de e-mail?')
        ds.create(first_name, last_name, email)
    elif opcao == 2:
        pass
    elif opcao == 7:
        break


print('Obrigado por usar nosso gerenciador de exentos!')
print('Até a Próxim!!!')
