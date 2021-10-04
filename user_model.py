from datetime import datetime

class UserModel:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.creation_date_time = datetime.now()
        self.check_name()
    
    def check_name(self):
        if self.first_name is None or len(self.first_name) == 0:
            raise Exception('O primeiro nome não foi fornecido')
        if self.last_name is None or len(self.last_name) == 0:
            raise Exception('O sobrenome não foi fornecido')
    
    def check_email(self):
        pass
    
    def update_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.check_name()
    
    def to_json(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'creation_date_time': self.creation_date_time
        }

    @staticmethod
    def from_json(json_data: dict):
        um = UserModel(
            first_name=json_data['first_name'],
            last_name=json_data['last_name'],
            email=json_data['email']
        )
        
        if 'creation_date_time' in json_data:
            um.creation_date_time = json_data['creation_date_time']
        
        return um
