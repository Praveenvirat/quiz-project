# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import AdminUser as auser


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user = auser.AdminUser()

    while True:
        print("Choose an option : ")
        print("1. User Action ")
        print("2. Admin Actions ")
        print("EXIT")
        choice = int(input())

        if choice == 1:
            print("1. Take Test")
            print("2. Display all user result")
            print("3. Display one user result")
            x = int(input("Choose: "))
            if x == 1:
                user.take_test()
            elif x == 2:
                user.display_user_results()
            elif x == 3:
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                user.display_particular_user_results(name, email)

        elif choice == 2:
            username = input("Admin: \nEnter Credentials \nUsername: ")
            password = input("password: ")
            if user.check_admin_login(username, password):
                user.add_question()

            else:
                print ("Wrong Credentials")

        else:
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
