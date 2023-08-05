# Student Management System

import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='your username',
                                     password='your password',
                                     database='SMS')


        # Create Student Table
        query = ('create table if not exists student(studentID int auto_increment primary key, Std_Name varchar(255), phone_Number numeric, email varchar(255), age int)')
        db = self.con.cursor()
        db.execute(query)
        print("Table Created!")


        # Insert Data into Table
    def insert_student(self,std_Name, phone_Number,email,age):
        query = ("insert into student(Std_Name, phone_Number,email,age) values ('{}',{},'{}',{})".format(std_Name, phone_Number,email,age))

        print(query)
        db = self.con.cursor()
        db.execute(query)
        self.con.commit()
        print("------")
        print("-> Data Inserted!")


        # Fetch All Data
    def fetch_all(self):
        query = ("Select * from student")
        db = self.con.cursor()
        db.execute(query)
        for row in db:
            
            print("StdName     : ", row[0])
            print("PhoneNumber : ", row[1])
            print("Email       : ", row[2])
            print("Age         : ", row[3])
            print("")
            print("")


        # Delete Student
    def delete_student(self,studentID):
        query = ("Delete from student where studentID = {}".format(studentID))
        print(query)
        db = self.con.cursor()
        db.execute(query)
        self.con.commit()
        print("------")
        print('-> Data Deleted!')


        # Update student
    def update_student(self, studentID, Std_Name, phone_number, email, age):
        query = ("update student set Std_Name = '{}', phone_number = {}, email = '{}', age = {} where studentID = {}".format(Std_Name , phone_number,email,age, studentID))
        print(query)
        db = self.con.cursor()
        db.execute(query)
        self.con.commit()
        print("------")
        print("-> Data Updated!")

# helper = DBHelper()
