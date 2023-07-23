#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge=[]
    
    def learn(self, information):
        self.knowledge.append(information)

# Creating an instance of the Student class
# my_student = Student("John", "Doe")

# Learning new information
# my_student.learn("Python is a programming language.")
# my_student.learn("Math is fun!")

# Accessing the knowledge list
# print(my_student.knowledge)  # Output: ['Python is a programming language.', 'Math is fun!']