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
        self.database.append(user_data.to_json())

    def update(self, email, first_name, last_name):
        user_found = next((x for x in self.database if x['email'] == email), None)
        if not user_found:
            raise Exception(f'Usuário com {email} não está cadastrado')
        user_data = UserModel.from_dict(user_found)
        user_data.update_name(first_name, last_name)
        self.database.remove(user_found)
        self.database.append(user_data.to_json())
    
    def get(self, first_name, last_name):
        pass
    
    def delete(self, email):
        pass
