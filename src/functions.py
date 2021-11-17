import re

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