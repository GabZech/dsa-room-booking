import re
import pandas as pd
from datetime import datetime

##########################################################
########## FUNCTIONS TO PROMPT USER INFORMATION ##########

def askStudentName():

    """
    This function will ask the user to provide their first and last name, separated by a space and in alphabetic letters only.
    It will then return the name given.

    Parameters:
    -------
    name: str

    Returns:
    -------
    name: str

    """

    while True:
        name = input("Please enter your full name: \n")
    
        if (any(x.isalpha() for x in name)
            and any(x.isspace() for x in name)
            and all(x.isalpha() or x.isspace() for x in name)
            and len(name) >= 5) == False: # require that the string contains at least one alpha, at least one space, only alphas and spaces, and at least 5 characters
            print("Error. Please provide your first and last name, separated by a space and in alphabetic letters only.")
        else:
            return name.upper()# we're happy with the value given and we're ready to exit the loop.

def askStudentID():

    """
    This function is designed to take input of a student ID number, and then check if 
    it is of length six. If the input is not of length six, it will print an error 
    message. If the input is not a number, it will print an error message.

    Parameters:
        None

    Returns:
        id: An integer representing the student's ID.

    Note:
        The function will keep looping until a 6 digit number is provided as input.
    """

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
            return id


def askStudentEmail():
    """
    askStudentEmail()

    Asks the user for their email address.

    Returns:
    output (str): The student's email address.
    """
    
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+") # regex that validates if string is an email address
    while True:
        email = input("Please enter your email: ")

        if email_regex.match(email) == None:
            print("Error. Please provide a valid email address.")
        else:
            return email
  

def askbookingInfoQuiet():
    """
    Function to ask the user whether they need a quiet room.

    Parameters:
        None

    Returns:
        quiet: A boolean value indicating whether the user needs a quiet room or not.
    """

    while True:
        
        quiet = input("Do you need a quiet room? yes/no: \n")
        if quiet.lower() == "yes" or quiet.lower() == "y":
            quiet = True
        elif quiet.lower() == "no" or quiet.lower() == "n":
            quiet = False
        else:
            print("Please write either yes or no")
            continue
        
        return quiet

def askbookingInfoTV():


    """
    Function which asks the user if a TV is needed.

    Parameters:
    None
    
    Returns:
    tv: Boolean, True if a TV is needed, False if not.
    """    
 
    while True:
        
        tv = input("Do you need a tv? yes/no: \n")
        if tv.lower() == "yes" or tv.lower()=="y":
            tv = True
        elif tv.lower() == "no" or tv.lower()=="n":
            tv = False
        else:
            print("Please write either yes or no")
            continue
        
        return tv

def askbookingInfoProjector():
    """
    Asks the user if they need a projector in their room.
    Returns a string, either "True" or "False".
    If the user does not write either "True" or "False", the function will keep asking.

    Parameters
    ----------

    Returns
    -------

    """


    while True:
        
        projector = input("Do you need a projector? yes/no: \n")
        if projector.lower() == "yes" or projector.lower()=="y":
            projector = True
        elif projector.lower() == "no" or projector.lower()=="n":
            projector = False
        else:
            print("Please write either yes or no")
            continue
        
        return projector


def askbookingInfoPlaces():
    """
    Asks the user for the number of places in the room.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    places : int64

    """  

    while True:
     try:
      places = int(input("Please enter the capacity of the room: \n"))
     except ValueError: # executes if input is not an integer
      print("Error. Please provide numbers only.")
      continue
     else: 
        return places
    



def askbookingInfoTime():  
   while True:
    try:
     date_entry = input("Enter a date in mm/dd/YYYY, HH format: \n")
     date_entry=datetime.strptime(date_entry,'%m/%d/%Y, %H')
     date_first = '01/01/2022, 00'
     date_first = datetime.strptime(date_first, '%m/%d/%Y, %H')
     date_last = '12/31/2022, 23'
     date_last = datetime.strptime(date_last, '%m/%d/%Y, %H')
    except ValueError:
     print("Incorrect format, please input \"month/day/year, hour \" e.g.: 12/01/2022, 10")
     continue
    if date_entry<date_first or date_entry>date_last:
        print("You can only pick dates from 01/01/2022, 00 till 12/31/2022, 23")
        continue
    else:
     return date_entry

