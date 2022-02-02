import json
from abc import ABC

class Model(ABC):
    file = "users.json"

    def check_email(self, email, all_users_data):
        for user in all_users_data:
            if email == user['Email']:
                return True
        return False

    def save(self):
        all_user_data = self.generation_dict()
        users = self.get_to_file()
        users.append(all_user_data)
        self.save_to_file(users)

    def generation_dict(self):
        all_user_data = self.__dict__
        return all_user_data

    @staticmethod
    def get_to_file():
        file = open('database/users.json', 'r')
        users = json.loads(file.read())
        file.close()
        return users
    @classmethod
    def get_all(cls):
        users = cls.get_to_file()
        return users

    def save_to_file(self, users):
        users = json.dumps(users)
        file = open('database/users.json', 'w')
        file.write(users)
        file.close()

    def users_up(self, users):
        with open('database/users.json', 'w') as file:
            file.write(json.dumps(users))

