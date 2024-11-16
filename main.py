global data, main_data
# Uses contacts files for handling the contact
filename = "contacts.csv"

f = open(filename, 'r')

main_data = f.read()

main_data = main_data.split('\n')

main_data = (list(filter(None, main_data)))


class contact_system():

    def __init__(self, user_id=0, name='', email='', mobile_no=0):

        self.user_id = user_id

        self.name = name

        self.email = email

        self.mobile_no = mobile_no

    # function to write file into the system
    def write_file(self, list_data):

        f = open(filename, "w")

        all_data = str()

        for data in list_data:
            all_data += data + '\n'

        f.write(all_data)

        f.close()

        return True

    # Function to show the contact list
    def show_contact(self):

        for data in main_data:
            split_data = data.split(',')
            print("Username :", split_data[0])
            print("Name :", split_data[1])
            print("Email :", split_data[2])
            print("Mobile-no :", split_data[3])
            print()

    # function to add contacts into the file by opening the file in append mode
    def add_contact(self):

        user_id = input("Enter Username :")

        name = input("Enter Name :")

        email = input("Enter Email :")

        mobile_no = input("Enter Mobile no :")

        data = user_id + ',' + name + ',' + email + ',' + mobile_no + '\n'

        f = open(filename, "a")

        f.write(data)

        f.close()

        print("Sucessfully Added the Contact!")

    # function to update the  contact
    def edit_contact(self, no):

        print("Username :", no)

        name = input("Enter Name :")

        email = input("Enter Email :")

        mobile_no = input("Enter Mobile no :")

        new_value = no + ',' + name + ',' + email + ',' + mobile_no

        for data in main_data:

            split_data = data.split(',')

            if no == split_data[0]:
                main_data[main_data.index(data)] = new_value

                self.write_file(main_data)

                print("Successfully edited the Data!")

                return True

        print("Try Again!")

    # function to delete the contact
    def remove_contact(self, no):

        for data in main_data:

            split_data = data.split(',')

            if no == split_data[0]:
                main_data.remove(data)

                break

        if (self.write_file(main_data)):

            print("Successfully Deleted!")

        else:

            print("Try Again please! ")

    def search_id(self, no):

        for data in main_data:

            split_data = data.split(',')

            if no == split_data[0]:
                return True

        return False

    # Function to search for a particular contact and display it
    def search_contact(self, no):

        for data in main_data:

            split_data = data.split(',')

            if no == split_data[0]:
                print("The contact is :")
                print("Username: ", split_data[0])
                print("Name: ", split_data[1])
                print("Email: ", split_data[2])
                print("Contact Number: ", split_data[3])
            else:
                print()


# while loop to not let the contact management system end without user choice.


class main():
    work = True

    def __init__(self):
        self

    def menu():

        my_class = contact_system()

        print('\n'""" >>>>>>> Contact Management System <<<<<<<<<<<<

    1=> Contact List

    2=> Add Contact

    3=> Edit Contact

    4=> Remove Contact

    5=> Search Contact

    6=> Exit

                    """)

        try:

            user_input = int(input("Please Enter option from above (1-5) : "))

        except ValueError:

            print("That is not true.")

        finally:

            print("")

        if user_input == 1:
            my_class.show_contact()



        elif user_input == 2:

            my_class.add_contact()

        elif user_input == 3:
            num = input("Enter Username for edit :")

            if my_class.search_id(num):

                my_class.edit_contact(num)

            else:

                print("Incorrect Username!!")



        elif user_input == 4:
            num1 = input("Enter Username to delete :")

            if my_class.search_id(num1):

                my_class.remove_contact(num1)

            else:

                print("Incorrect Username!!")

        elif user_input == 5:

            num1 = input("Enter Username for Search :")

            my_class.search_contact(num1)



        elif user_input == 6:
            print("Thankyou for Using the Contact Management System")
            work = False




        else:
            print("Invalid Input!!")

    while work:
        menu()
