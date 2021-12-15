import pandas as pd


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
        print("We are sorry, there are no rooms with such criteria, try again")
        
        

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


