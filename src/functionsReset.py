import pandas as pd


#####################################
########## OTHER Reset ##########

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
