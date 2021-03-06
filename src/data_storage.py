from user_model import UserModel


class DataStorage:
    database = list()

    def __init__(self):
        pass

    def create(self, first_name: str, last_name: str, email: str):
        item_found = next((x for x in self.database if x['email'] == email), None)
        if item_found:
            raise Exception(f'Usuário já cadastrado com o e-mail {email}')
        user_data = UserModel(first_name, last_name, email)
        user_data_json = user_data.to_json()
        self.database.append(user_data_json)
        return user_data_json

    def update(self, email, first_name, last_name):
        user_found = next((x for x in self.database if x['email'] == email), None)
        if not user_found:
            raise Exception(f'Usuário com {email} não está cadastrado')
        user_data = UserModel.from_json(user_found)
        user_data.update_name(first_name, last_name)
        self.database.remove(user_found)
        self.database.append(user_data.to_json())
        return user_data.to_json()

    def get(self, first_name, last_name):
        result = []
        for user in self.database:
            if user['first_name'] == first_name and user['last_name'] == last_name:
                result.append(user)
        return result

    def get_email(self, email):
        for user in self.database:
            if user['email'] == email:
                return user
        return None

    def delete(self, email):
        result = self.get_email(email=email)
        if not result:
            raise Exception(f'Usuário inexistente com o e-mail {email} ')
        else:
            self.database.remove(result)
