#!/usr/bin/env python

from user import User
import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge=knowledge

    def teach(self):
        # we can add import random inside the method
        return random.choice(self.knowledge)
    
# Create an instance of the Teacher class
# my_teacher = Teacher("John", "Doe")

# Get a random topic that the teacher can teach
# taught_topic = my_teacher.teach()

# Output the result
# print(f"{my_teacher._first_name} {my_teacher._last_name} can teach: {taught_topic}")