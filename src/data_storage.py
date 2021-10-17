from user_model import UserModel
from typing import List


class DataStorage:
    database = List[dict]

    def __init__(self):
        pass
    
    def create(self, first_name, last_name, email):
        item_found = [x for x in self.database if x['email'] == email]
        if item_found:
            raise Exception(f'Usuário já cadastrado com o e-mail {email}')
        user_data = UserModel(first_name, last_name, email)
        self.database[user_data.email] = user_data.to_json()

    def update(self, email, first_name, last_name):
        if email not in self.database:
            raise Exception(f'Usuário {email} não está cadastrado')
        user_data_dict = self.database['email']
        user_data = UserModel.from_dict(user_data_dict)
        user_data.update_name(first_name, last_name)
        self.database['email'] = user_data.to_json()
    
    def list_all(self, sort_type):
        pass
    
    def get(self, first_name, last_name):
        result = []
        for user in self.database:
            if user['first_name'] == first_name and user['last_name'] == last_name:
                result.append(user)
        return result
    
    def delete(self, email):
        pass
