import re
import pandas as pd


##########################################################
########## FUNCTIONS TO PROMPT USER INFORMATION ##########

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
  
def askbookingInfoQuite():
     quite= input("Do you need a quite room? True/False: \n")
     while quite != "True" and quite != "False":
         print("Please write either True or False")
         quite= input("Do you need a quite room? True/False: \n")
     return quite
    
def askbookingInfoTV():
    tv = input("Do you need a TV in your room? True/False: \n")
    while tv != "True" and tv != "False":
        print("Please write either True or False")
        tv = input("Do you need a TV in your room? True/False: \n")
    return tv
 
def askbookingInfoProjector():
    projector = input("Do you need a projector in your room? True/False: \n" )
    while projector!= "True" and projector != "False":
        print("Please write either True or False")
        projector = input("Do you need a TV in your room? True/False: \n")
    return projector

def askbookingInfoPlaces():   
    while True:
     try:
      places = int(input("Please enter the capacity of the room: \n"))
     except ValueError: # executes if input is not an integer
      print("Error. Please provide numbers only.")
      continue
     else: 
        return places

###################################################
########## FUNCTIONS TO HANDLE DATABASES ##########

def readRooms():
    df = pd.read_csv("../data/processing/rooms.csv", dtype={"name": str}, parse_dates=["date_time"])
    return df

def readBookings():
    df = pd.read_csv("../data/processing/bookings.csv", dtype={"room_name": str}, parse_dates=["room_datetime"])
    return df


#######################################################
########## FUNCTIONS TO PROMPT USER DECISION ##########
    
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
    df_rooms = pd.read_excel("../data/raw/rooms.xlsx")
    df_rooms.to_csv("../data/processing/rooms.csv", index = False)
    
    df_bookings = pd.read_excel("../data/raw/bookings.xlsx")
    df_bookings.to_csv("../data/processing/bookings.csv", index = False)
    
    print("bookings reset")
