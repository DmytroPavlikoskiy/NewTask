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
                what_to_search = input('By Which Parametr you want to search: ')
                search_str = input('Search: ')
                self.search_by(search_str, what_to_search)
            elif menu_flag == 4:
                self.update_user()


    def user_add(self):
        all_users_data = Users.get_all()
        if len(all_users_data) > 0:
            id = all_users_data[-1]['id'] + 1
        else:
            id = 1
        first_name = input("First Name :")
        last_name = input("Last Name :")
        Email = input("Email")
        useradd = Users(id, first_name, last_name, Email)
        useradd.save()

    def get_all(self):
        users = Users.get_all()
        for user in users:
            print("User #" + str(user['id']))
            print("First Name: " + user['first_name'])
            print("Last Name: " + user['last_name'])
            print("Email: " + user['Email'])

    def search_by(self, search_str, what_to_search):
        users = Users.get_all()
        for user in users:
            if str(user[what_to_search]).lower() == str(search_str).lower():
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['Email'])

    def update_user(self):
        id = int(input("Type id of user which you want to update: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        Email = input("Email: ")
        users = Users.get_all()
        for user in users:
            if user['id'] == id:
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['Email'] = Email
        userup = Users(id, first_name, last_name, Email)
        userup.users_up(users)


