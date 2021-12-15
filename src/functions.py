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
            and all(x.isalpha() or x.isspace() for x in name)) == False: # require that the string contains at least one alpha, at least one space, and only alphas and spaces
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
            print("Please write either True or False")
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
     date_entry = input("Enter a date in mm/dd/YY, HH format: \n")
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
 
    
###################################################
########## FUNCTIONS TO HANDLE DATABASES ##########

def readRooms():

    """
    Reads the rooms.csv file into a pandas dataframe.

    Parameters:
        None

    Returns:
        A pandas dataframe containing the rooms.csv file.
    """

    df = pd.read_csv("../data/processing/rooms.csv", dtype={"name": str}, parse_dates=["date_time"])
    return df


def readBookings():
    """
    Reads the bookings.csv file and returns a pandas dataframe.

    Parameters:
        None

    Returns:
        pandas dataframe
    """
    df = pd.read_csv("../data/processing/bookings.csv", dtype={"room_name": str}, parse_dates=["room_datetime"])
    return df

def readRoomsTest():
    df = pd.read_csv("../data/processing/roomsTest.csv", dtype={"name": str}, parse_dates=["date_time"])
    return df





#######################################################
########## FUNCTIONS TO PROMPT USER DECISION ##########
    
def chooseRoom(df):
    '''

    This function takes a dataframe as input and returns the index of the chosen room and the name of the room.
    The function also prints the available rooms and their number of available places.
    The function asks the user to choose a room.
    If the user provides a room that is not in the list of available rooms, the function prints an error message and asks the user to provide a valid room.
    If there are no available rooms, the function prints an error message and asks the user to try again.
    The function returns the index of the chosen room and the name of the room.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    index : int64
    chosen_room : str

    '''
    

    num_avl_rooms = df.shape[0] # number of rows = number of available rooms
    room_names_list = df['name'].tolist()
    room_available_places = df['available_places'].tolist()
    
    if num_avl_rooms == 0:
        print("We are sorry, there are no rooms with such criterias, try again")
        
        

    else:
        print(f"There are {num_avl_rooms} available rooms:")
        i = 0 
        while i < len(room_names_list):
            print(f"Room {room_names_list[i]} has {room_available_places[i]} places available at the chosen time and date")
            i += 1

        while True:
            chosen_room = input("Which room would you like to book? ")

            if chosen_room not in room_names_list: 
                print("Error. Please provide a valid room number.")
            else:
                index = df.loc[df["name"] == chosen_room].index.values[0]
                return index, chosen_room


def cancelBooking(df):

    """
    Cancels a booking.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the bookings.

    Returns
    -------
    None

    """
    
    room_names_list = df['room_name'].tolist()
    room_places_list = df['room_places'].tolist()
    room_datetime_list = df['room_datetime'].tolist()
    
    print("\nThe following bookings were found:")
    
    for i, val in enumerate(room_names_list):
        print(f"Booking number {i+1}: on {room_datetime_list[i].strftime('%A %x')} at {room_datetime_list[i].strftime('%I %p')} -> {room_places_list[i]} place(s) in room {room_names_list[i]}")
        
    while True:
        chosen_booking = int(input("Which booking number would you like to cancel? "))
        chosen_booking = chosen_booking-1
      
        if chosen_booking not in [*range(0, len(room_names_list), 1)]:
            print("Error. Please provide a valid booking number.")
        else:
            # read rooms file
            df_rooms = readRooms()
            
            # get row corresponding to chosen booking
            df_temp = df.iloc[[chosen_booking]]

            # extract information from this row
            booked_room_name = df_temp["room_name"].values[0]
            booked_datetime = df_temp["room_datetime"].values[0]
            booked_places = df_temp["room_places"].values[0]
            
            # replace availability in rooms.csv
            booked_room_index = df_rooms[(df_rooms.name == booked_room_name) &
                                         (df_rooms.date_time == booked_datetime)].index.values[0] # gets corresponding index value in rooms.csv
            df_rooms.at[booked_room_index, "available_places"] = df_rooms.iloc[booked_room_index]["available_places"] + booked_places
            df_rooms.to_csv("../data/processing/rooms.csv", index = False)
            
            # delete entry on bookings.xlsx
            df_bookings = readBookings()
            print("\nThe following booking has been deleted: ")
            print(f"Booking number {chosen_booking+1}: on {room_datetime_list[chosen_booking].strftime('%A %x')} at {room_datetime_list[chosen_booking].strftime('%I %p')} -> {room_places_list[chosen_booking]} place(s) in room {room_names_list[chosen_booking]}")
            df_bookings.drop(index=chosen_booking, inplace=True)
            df_bookings.to_csv("../data/processing/bookings.csv", index=False)
            
            break


#####################################
########## OTHER FUNCTIONS ##########

def resetBookings():
    """
    Resets the bookings.csv and rooms.csv files to their original state.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """

    df_rooms = pd.read_excel("../data/raw/rooms.xlsx")
    df_rooms.to_csv("../data/processing/rooms.csv", index = False)
    
    df_bookings = pd.read_excel("../data/raw/bookings.xlsx")
    df_bookings.to_csv("../data/processing/bookings.csv", index = False)
    
    print("bookings reset")
