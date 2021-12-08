import functions as fn
import classes as cl
import datetime
import time

'''
TO-DOs

- Create functions for user to input values for bookingInfo
        - Note: des_datetime must be in datetime format e.g. "01.01.2022  10:00:00"

- Create more day and hour entries for every room on the csv file (currently only for 01.01.2022 and 10am)
- Allow users to choose 1 or 2h for booking a room
- Show how many spaces available per room
- set a timer between booking and showing options
- what is our default, what if there is 0 rooms? stop the program, go back to "CHOICE"

'''


# ask for student details
print("\n\n----- WELCOME ----- \nPlease enter the following details to proceed.")
student = cl.Student(fn.askStudentName(), fn.askStudentID(), fn.askStudentEmail())
#student = cl.Student("Gab", 123456, "x@x.com")
#room_datetime = datetime.datetime.strptime("01.01.2022  10:00:00","%d.%m.%Y %H:%M:%S")


# start programme
while True:
    try:
        choice = int(input("\n\n----- OPTIONS ----- \n1: Book a room \n2: Cancel a booking \n3: Exit \n\nPlease type the number of your choice to proceed: "))
    except ValueError: # executes if input is not an integer
        print("Error. Please provide numbers only.")
        time.sleep(2) 
        continue
  
    if choice == 1:
    
        print("\n\n----- BOOK A ROOM -----")
        
        # import dataframe of rooms
        df_rooms = fn.readRooms()
        
        # ask for booking information
        booking = cl.bookingInfo(quiet=fn.askbookingInfoQuiet(),
                                 tv=fn.askbookingInfoTV(), 
                                 projector=fn.askbookingInfoProjector(), 
                                 places=fn.askbookingInfoPlaces(), 
                                 datetime = datetime.datetime(year=2022, month=1, day=1, hour=10))
        


        # find matching rooms
        df_match = df_rooms[(df_rooms.date_time == booking.datetime) &
                            (df_rooms.available_places >= booking.places) & # return rooms with same or higher number of availabe places
                            (df_rooms.quiet == booking.quiet) &
                            (df_rooms.tv == booking.tv) &
                            (df_rooms.projector == booking.projector)
                            ]
        
        # choose room
        chosen_room_index, chosen_room_name = fn.chooseRoom(df_match)

        #decrease room availability in original
        df_rooms = fn.readRooms() # re-read dataframe to avoid another user having already booked a place in same room during this time (thus preventing overbooking)
        
        if df_rooms.iloc[chosen_room_index]["available_places"] >= booking.places: # if still available places
            
            # decrease number of available places and save dataframe
            df_rooms.at[chosen_room_index, "available_places"] = df_rooms.iloc[chosen_room_index]["available_places"] - booking.places 
            df_rooms.to_csv("../data/processing/rooms.csv", index = False)
            print(f"\n{booking.places} place(s) have been succesfully booked in room {chosen_room_name} on {booking.datetime.strftime('%A %x')} at {booking.datetime.strftime('%I %p')}")
            
            # save booking info to bookings.xslx
            row = [student.name, student.id, student.email, chosen_room_name, booking.places, booking.datetime]
            df_bookings = fn.readBookings()
            df_bookings.loc[len(df_bookings)] = row
            df_bookings.to_csv("../data/processing/bookings.csv", index=False)
            
            time.sleep(3) 
            
            continue
            
        else: # this is a simple overbooking prevention
            print("\nSomeone has just made a booking for the same room at the given time and date. \nThe room is no available for the chosen number of places anymore. \nPlease try again and choose another room.")
            continue
        

    elif choice == 2:
        # CANCEL BOOKING
        print("\n\n----- CANCEL BOOKING -----")
        df_bookings = fn.readBookings()
        
        # show booked rooms and prompt user to choose which to cancel
        df_match = df_bookings[(df_bookings["student_name"] == student.name) &
                               (df_bookings["student_id"] == student.id) &
                               (df_bookings["room_datetime"] >= datetime.datetime.now())] # show only future bookings
        
        fn.cancelBooking(df_match)
        
        time.sleep(3) 
        
        continue
    
    elif choice == 3:
        
        print("\nExiting application. Goodbye!")
        
        break
    
    else:
        print("\nPlease choose a valid number.")
        continue

#%%
#fn.resetBookings()
df_rooms = fn.readRooms()
