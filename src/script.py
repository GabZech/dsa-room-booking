import functions as fn
import classes as cl
import pandas as pd
import datetime

'''
TO-DOs

- Create functions for user to input values for des_datetime, des_places, des_quiet, des_tv, des_projector
        - Note: des_datetime must be in datetime format e.g. "01.01.2022  10:00:00"

- Create more day and hour entries for every room on the excel file (currently only for 01.01.2022 and 10am)

- Change data/processing files from xlsx to csv 

- Create welcome page where student is asked if they want to book or cancel a room

'''


#%%

# ask for student details
# student = cl.Student(fn.askStudentName(), fn.askStudentID(), fn.askStudentEmail())
student = cl.Student("Gab", 123456, "x@x.com")

#room_datetime = datetime.datetime.strptime("01.01.2022  10:00:00","%d.%m.%Y %H:%M:%S")

#%%

print("\nBOOK A ROOM")

# import dataframe of rooms
df = pd.read_excel("../data/processing/rooms.xlsx", dtype={"name": str})

# given user input, create object with all matching available rooms

# user input ("des" = "desired)
booking = cl.bookingInfo(places = 1,
                        datetime = datetime.datetime(year=2022, month=1, day=1, hour=10, minute=0, second=0),
                        quiet = True,
                        tv = False,
                        projector = False
                        )
# des_datetime = 
# des_places = 1
# des_quiet = True
# des_tv = False
# des_projector = False

# find matching rooms
df_match = df[(df.date_time == booking.datetime) &
    (df.available_places >= booking.places) & # return rooms with same or higher number of availabe places
    (df.quiet == booking.quiet) &
    (df.tv == booking.tv) &
    (df.projector == booking.projector)
    ]

# choose room
chosen_room_index, chosen_room_name = fn.chooseRoom(df_match)


#%%
#decrease room availability in original
df = pd.read_excel("../data/processing/rooms.xlsx", dtype={"name": str}) # re-read dataframe to avoid another user having already booked a place in same room during this time (thus preventing overbooking)

if df.iloc[chosen_room_index]["available_places"] >= booking.places: # if still available places
    
    # decrease number of available places and save dataframe
    df.at[13, "available_places"] = df.iloc[chosen_room_index]["available_places"] - booking.places 
    df.to_excel("../data/processing/rooms.xlsx", index = False)
    print(f"\n{booking.places} place(s) have been succesfully booked in room {chosen_room_name} on {booking.datetime.strftime('%A %x')} at {booking.datetime.strftime('%I %p')}")
    
    # save booking info to bookings.xslx
    row = [student.name, student.id, student.email, chosen_room_name, booking.places, booking.datetime]
    df_bookings = pd.read_excel("../data/processing/bookings.xlsx", dtype={"room_name": str})
    df_bookings.loc[len(df_bookings)] = row
    df_bookings.to_excel("../data/processing/bookings.xlsx", index=False)
    
else: # this is a simple overbooking prevention
    print("Someone has just made a booking for the same room at the given time and date. \nThe room is no available for the chosen number of places anymore. \nPlease try again and choose another room.")


#%%

# CANCEL BOOKING
print("\nCANCEL BOOKING")
df_bookings = pd.read_excel("../data/processing/bookings.xlsx", dtype={"room_name": str})

# show booked rooms and prompt user to choose which to cancel
df_match = df_bookings[(df_bookings["student_name"] == student.name) &
                       (df_bookings["student_id"] == student.id) &
                       (df_bookings["room_datetime"] >= datetime.datetime.now())] # show only future bookings

def chooseBooking(df):
    
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
            df_temp = df.iloc[[chosen_booking]]
            
            # replace availability in rooms.xlsx
            df_rooms = pd.read_excel("../data/processing/rooms.xlsx", dtype={"name": str})

            room_name = df_temp["room_name"].values[0]
            datetime = df_temp["room_datetime"].values[0]
            booked_places = df_temp["room_places"].values[0]
            
            # now change based on the values above
            # WORK HERE ######################################

            
            # delete entry on bookings.xlsx
            df_bookings = pd.read_excel("../data/processing/bookings.xlsx")
            print("\nThe following booking has been deleted: ")
            print(f"Booking number {chosen_booking+1}: on {room_datetime_list[chosen_booking].strftime('%A %x')} at {room_datetime_list[chosen_booking].strftime('%I %p')} -> {room_places_list[chosen_booking]} place(s) in room {room_names_list[chosen_booking]}")
            df_bookings.drop(index=chosen_booking, inplace=True)
            df_bookings.to_excel("../data/processing/bookings.xlsx", index=False)
            

            
            break


chooseBooking(df_match)

#%%
df = df_bookings.iloc[[0]]
print(df["room_name"].values[0])

# fn.resetBookings()