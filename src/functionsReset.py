import pandas as pd


#####################################
########## OTHER Reset ##########

def resetBookings():
    
    """
    This function resets the bookings.csv and rooms.csv files to their original state.

    Parameters
    ----------
    df_rooms : excel file
    df_bookings : excel file

    Returns
    -------
    df_rooms : excel file
    df_bookings : excel file

    """

    df_rooms = pd.read_excel("../data/raw/rooms.xlsx")
    df_rooms.to_csv("../data/processing/rooms.csv", index = False)
    
    df_bookings = pd.read_excel("../data/raw/bookings.xlsx")
    df_bookings.to_csv("../data/processing/bookings.csv", index = False)
    
    print("bookings reset")
