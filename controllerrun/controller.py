from NewTask.models.users import Users

class ControllerRun:

    def conRun(self):

        while True:
            print("1. Add New User\n"
                  + "2. Get All Users\n"
                  + "3. Search\n"
                  + "4. Update User By Id"
                  )
            menu_flag = int(input("Type your choose: "))
            if menu_flag == 1:
                self.user_add()
            elif menu_flag == 2:
                self.get_all()
            elif menu_flag == 3:
                self.parameters = input('By Which Parametr you want to search first_name, last_name or Email: ')
                self.choose = input('Search: ')
                self.search_by()
            elif menu_flag == 4:
                self.parameters = input('By Which Parametr you want to search first_name, last_name or Email: ')
                self.choose = input('Your Choose: ')
                self.type_id = int(input("Type id of user which you want to update: "))
                self.update_user()



    def user_add(self):
        first_name = input("First Name :")
        last_name = input("Last Name :")
        Email = input("Email")
        useradd = Users(first_name, last_name, Email)
        useradd.save()

    def get_all(self):
        sql = Users.get_all()
        print(sql)

    def search_by(self):
        sql = Users.search_by(self.parameters, self.choose )
        print(sql)

    def update_user(self):
        result = Users.update_user(self.type_id, self.parameters, self.choose)
        print(result)



