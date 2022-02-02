from NewTask.framework.models import Model

class Users(Model):
    file = "users.json"

    def __init__(self, id, first_name, last_name, Email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.Email = Email
