from data_storage import DataStorage


def main():
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
            first_name = input('Qual o primeiro nome do usuário? ')
            last_name = input('qual o último nome da pessoa? ')
            email = input('Qual o endereço de e-mail? ')
            print('\n Cadastrando Usuário \n')

            try:
                result = ds.create(first_name=first_name, last_name=last_name, email=email)
                print('Usuário cadastrado com sucesso:')
                print(f"({result['creation_date_time'].strftime('%d/%m/%Y %H:%M:%S')}) {result['first_name']} {result['last_name']} \n\n")
            except Exception as exc:
                print(f'Ocorreu o seguinte erro ao tentar cadastrar o usuário de e-mail {email}: {exc}\n')

        elif opcao == 2:
            user_list = ds.database
            user_list.sort(key=lambda item: item['creation_date_time'], reverse=False)
            for user in user_list:
                print(f"Nome: {user['first_name']}")
                print(f"Sobrenome: {user['last_name']}")
                print(f"Email: {user['email']}\n\n")

        elif opcao == 3:
            user_list = ds.database
            user_list.sort(key=lambda item: item['first_name'], reverse=False)
            for user in user_list:
                print(f"Nome: {user['first_name']}")
                print(f"Sobrenome: {user['last_name']}")
                print(f"Email: {user['email']}\n\n")

        elif opcao == 4:
            first_name = input('Digite o primeiro nome do usuário desejado: ')
            last_name = input('Digite o sobrenome do usuário desejado: ')
            result = ds.get(first_name=first_name, last_name=last_name)
            if len(result) == 0:
                print("Nenhum usuário cadastrado com esse nome!")
            else:
                for user in result:
                    print(f"Nome: {user['first_name']} {user['last_name']}")

        elif opcao == 5:
            email = input('Digite o email desejado: ')
            try:
                ds.delete(email)
                print('Usuário deste email deletado com sucesso!')
            except Exception as exc:
                print(f'Ocorreu o erro: {exc}')

        elif opcao == 6:
            email = input('Digite o email do usuario? ')
            first_name = input('Qual o primeiro nome do usuario? ')
            last_name = input('Digite o sobrenome do usuario? ')
            try:
                result = ds.update(email=email, first_name=first_name, last_name=last_name)
                print('Usuário atualizado com sucesso:')
                print(f"({result['creation_date_time'].strftime('%d/%m/%Y %H:%M:%S')}) {result['first_name']} {result['last_name']}\n\n")
            except Exception as exc:
                print(f'Ocorreu o erro: {exc}')

        elif opcao == 7:
            break


    print('Obrigado por usar nosso gerenciador de eventos!')
    print('Até a Próxima!!!')


if __name__ == '__main__': 
    main()
