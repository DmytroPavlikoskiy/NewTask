from NewTask.framework.models import Model


class Users(Model):
    table = "users"

    def __init__(self, id, first_name, last_name, Email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.Email = Email

    def save(self):
        cursor = self.connects()
        sql = "INSERT INTO users(first_name, last_name, Email)" \
              "VALUES ('%s', '%s', '%s')" % (self.first_name, self.last_name, self.Email)
        try:
            cursor.execute(sql)
            self.connect.commit()

        except:
            self.connect.rollback()
