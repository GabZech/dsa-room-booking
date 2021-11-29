import re
import pandas as pd

def askStudentName():

  while True:
    name = input("Please enter your full name: ")
    
    if (any(x.isalpha() for x in name)
    and any(x.isspace() for x in name)
    and all(x.isalpha() or x.isspace() for x in name)) == False: # require that the string contains at least one alpha, at least one space, and only alphas and spaces
      print("Error. Please provide your first and last name, separated by a space and in alphabetic letters only.")
    else:
      return name # we're happy with the value given and we're ready to exit the loop.

  


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
        return id




def askStudentEmail():
  
  email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+") # regex that validates if string is an email address

  while True:
    email = input("Please enter your email: ")

    if email_regex.match(email) == None:
      print("Error. Please provide a valid email address.")
    else:
      return email
  
    
  
    
def chooseRoom(df):
    '''
    Prompts user to choose from a list of available rooms.

    Parameters
    ----------
    df : dataframe
        DESCRIPTION.

    Returns
    -------
    index : int64
    chosen_room : str
        DESCRIPTION.

    '''
    num_avl_rooms = df.shape[0] # number of rows = number of available rooms
    room_names_list = df['name'].tolist()
    room_names_string = "\n".join(map(str, room_names_list))
    
    print(f"There are {num_avl_rooms} available rooms:\n{room_names_string}")
    
    while True:
        chosen_room = input("Which would you like to book? ")
      
        if chosen_room not in room_names_list: 
            print("Error. Please provide a valid room number.")
        else:
            index = df.loc[df["name"] == chosen_room].index.values[0]
            return index, chosen_room
        

def resetBookings():
    df_rooms = pd.read_excel("../data/raw/rooms.xlsx")
    df_rooms.to_excel("../data/processing/rooms.xlsx", index = False)
    
    df_bookings = pd.read_excel("../data/raw/bookings.xlsx")
    df_bookings.to_excel("../data/processing/bookings.xlsx", index = False)
