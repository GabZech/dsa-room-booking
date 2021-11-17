import re

# %%

class Room:

    def __init__(self, name, capacity, quiet, tv, projector):
        self.__name = name
        self.__capacity = capacity
        self.__quiet = quiet 
        self.__tv = tv
        self.__projector = projector

# create rooms
room1=Room("2.31", 2, True, True, False)
room2=Room("2.32", 3, True, False, False)
room3=Room("2.35", 8, False, False, False)
room4=Room("2.31", 2, True, True, False)
room5=Room("3.22", 4, True, False, True)
room6=Room("3.47", 4, False, False, False)
room7=Room("2.71", 7, False, True, False)
room8=Room("3.10", 7, False, True, False)
room9=Room("2.32", 3, True, False, False)
room10=Room("3.33", 5, True, False, False)
room11=Room("3.35", 12, True, False, True)
room12=Room("3.40", 15, False, True, True)
room13=Room("3.50", 17, False, False, False)
room14=Room("3.60", 4, True, False, False)


# %%

class Student:
     def __init__(self, name, id, email):
                       self._name = name
                       self._id = id
                       self._email = email

## create getters for Student name, id and email

def askStudentName():

  while True:
    name = input("Please enter your full name: ")
    
    if (any(x.isalpha() for x in name)
    and any(x.isspace() for x in name)
    and all(x.isalpha() or x.isspace() for x in name)) == False: # require that the string contains at least one alpha, at least one space, and only alphas and spaces
      print("Error. Please provide your first and last name, separated by a space and in alphabetic letters only.")
    else:
      break # we're happy with the value given and we're ready to exit the loop.

  return name


def askStudentID():

  while True:
    try:
      id = int(input("Please enter your student ID: "))
    except ValueError: # executes if input is not an integer
      print("Error. Please provide numbers only.")
      continue

    if len(str(id)) != 6: # executes if input is not of length 6
      print("Error. The ID provided does not have 6 digits.")
      continue

    else: 
      break

  return id


def askStudentEmail():
  
  email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+") # regex that validates if string is an email address

  while True:
    email = input("Please enter your email: ")

    if email_regex.match(email) == None:
      print("Error. Please provide a valid email address.")
    else:
      break

  return email


new_student = Student(askStudentName(), askStudentID(), askStudentEmail())

