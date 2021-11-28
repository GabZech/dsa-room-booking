import functions as fn
import classes as cl
import pandas as pd
import datetime

'''
TO-DOs

- Create functions for user to input values for des_datetime, des_places, des_quiet, des_tv, des_projector

- Create more day and hour entries for every room on the excel file (currently only for 01.01.2022 and 10am)

- Create database containing students information and info on which rooms they have booked

'''


#%%

# ask for student details
student = cl.Student(fn.askStudentName(), fn.askStudentID(), fn.askStudentEmail())


#%%

# import dataframe of rooms
df = pd.read_excel("../data/processing/rooms.xlsx", dtype={"name": str})

# given user input, create object with all matching available rooms

# user input ("des" = "desired)
des_datetime = datetime.datetime(year=2022, month=1, day=1, hour=10, minute=0, second=0)
des_places = 1
des_quiet = True
des_tv = False
des_projector = False

# find matching rooms
df_match = df[(df.date_time == des_datetime) &
    (df.available_places >= des_places) & # return rooms with same or higher number of availabe places
    (df.quiet == des_quiet) &
    (df.tv == des_tv) &
    (df.projector == des_projector)
    ]

# choose room
chosen_room_index, chosen_room_name = fn.chooseRoom(df_match)


#%%
#decrease room availability in original
df = pd.read_excel("../data/processing/rooms.xlsx", dtype={"name": str}) # re-read dataframe to avoid another user having already booked a place in same room (thus lightly preventing overbooking)

if df.iloc[chosen_room_index]["available_places"] >= des_places: # if still available places
    df.at[13, "available_places"] = df.iloc[chosen_room_index]["available_places"] - des_places # decrease number of available places
    
    df.to_excel("../data/processing/rooms.xlsx", index = False)
    
    print(f"{des_places} place(s) have been succesfully booked in room {chosen_room_name} on {des_datetime.strftime('%A %x')} at {des_datetime.strftime('%I %p')}")
    
else: # this is a simple overbooking prevention
    print("Someone has just made a booking for the same room at the given time and date. \nThe room is no available for the chosen number of places anymore. \nPlease try again and choose another room.")


#%%

