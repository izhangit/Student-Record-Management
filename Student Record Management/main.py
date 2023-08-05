
from dbhelper import DBHelper

def main():
    db = DBHelper()

    while True:
        print("---------STUDENT MANAGRMENT SYSTEM-----------")
        print()
        print("PRESS 1 to Insert New Student")
        print("PRESS 2 to Display all Student")
        print("PRESS 3 to Delete Student")
        print("PRESS 4 to update Student")
        print("PRESS 5 to Exit Program")
        print()

        try:
            choice = int(input("Enter the Number : "))
            print()

            if (choice == 1):

                sName =      input("Enter StudentName         : ")
                sphone = int(input("Enter the Phone No        : "))
                semail =     input("Enter your Email          : ")
                sage =   int(input("Enter your Age            : "))
                # Insert 
                db.insert_student(sName, sphone,semail,sage)    
                
            elif (choice == 2):
                # display
                db.fetch_all()

            elif (choice == 3):
                user_id = int(input("Enter StudentID to which you want to delete : "))
                # delete
                db.delete_student(user_id)
                
            elif (choice == 4):
                stdname = input("Enter New name       : ")
                sphone =  int(input("Enter New phone No    : "))
                semail = input("Enter New Email          : ")
                sage = int(input("Enter Your New Age     : "))
                # update
                db.update_student(stdname, sphone,semail,sage)
                
            elif (choice == 5):
                print("Bye! this program is exited")
                print()
                break
                # Exit 
            else:
                print("Invalid Input. Try again!")

        except Exception as e:
            print(e)
            print("Invalid Details! Try again")
            print()
            print()

if __name__ == "__main__":
    main()

        