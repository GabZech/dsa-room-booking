import functionsUser as fnu
import functionsDecision as fnd
import classes as cl
import datetime
import time


# ask for student details
print("\n\n----- WELCOME ----- \nPlease enter the following details to proceed.")
student = cl.Student(fnu.askStudentName(), fnu.askStudentID(), fnu.askStudentEmail())
#student = cl.Student("Gab", 123456, "x@x.com")
#room_datetime = datetime.datetime.strptime("01.01.2022  10:00:00","%d.%m.%Y %H:%M:%S")


# start programme
while True:
    try:
        choice = int(input("\n\n----- OPTIONS ----- \n1: Book a room \n2: Cancel a booking \n3: Exit \n\nPlease type the number of your choice to proceed: "))
    except ValueError: # executes if input is not an integer
        print("Error. Please provide numbers only (from 1 to 3).")
        time.sleep(2) 
        continue
  
    if choice == 1:
    
        print("\n\n----- BOOK A ROOM -----")
        
        # import dataframe of rooms
        df_rooms = fnd.readRooms()
        
        # ask for booking information
        booking = cl.bookingInfo(quiet=fnu.askbookingInfoQuiet(),
                                 tv=fnu.askbookingInfoTV(), 
                                 projector=fnu.askbookingInfoProjector(), 
                                 places=fnu.askbookingInfoPlaces(), 
                                 datetime = fnu.askbookingInfoTime())
        


        # find matching rooms
        df_match = df_rooms[(df_rooms.date_time == booking.datetime) &
                            (df_rooms.available_places >= booking.places) & # return rooms with same or higher number of availabe places
                            (df_rooms.quiet == booking.quiet) &
                            (df_rooms.tv == booking.tv) &
                            (df_rooms.projector == booking.projector)
                            ]
        if len(df_match)==0:
            print("We are sorry, there are no rooms with such criterias, please try again later")
            break   
        
        # choose room
        chosen_room_index, chosen_room_name = fnd.chooseRoom(df_match)
        

        #decrease room availability in original
        df_rooms = fnd.readRooms() # re-read dataframe to avoid another user having already booked a place in same room during this time (thus preventing overbooking)
        
        if df_rooms.iloc[chosen_room_index]["available_places"] >= booking.places: # if still available places
            
            # decrease number of available places and save dataframe
            df_rooms.at[chosen_room_index, "available_places"] = df_rooms.iloc[chosen_room_index]["available_places"] - booking.places 
            df_rooms.to_csv("../data/processing/rooms.csv", index = False)
            print(f"\n{booking.places} place(s) have been succesfully booked in room {chosen_room_name} on {booking.datetime.strftime('%A %x')} at {booking.datetime.strftime('%I %p')}")
            
            # save booking info to bookings.xslx
            row = [student.name, student.id, student.email, chosen_room_name, booking.places, booking.datetime]
            df_bookings = fnd.readBookings()
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
        df_bookings = fnd.readBookings()
        
        # show booked rooms and prompt user to choose which to cancel
        df_match = df_bookings[(df_bookings["student_name"] == student.name) &
                               (df_bookings["student_id"] == student.id) &
                               (df_bookings["room_datetime"] >= datetime.datetime.now())] # show only future bookings
        
        fnd.cancelBooking(df_match)
        
        time.sleep(3) 
        
        continue
    
    elif choice == 3:
        
        print("\nExiting application. Goodbye!")
        
        break
    
    else:
        print("\nPlease choose a valid number.")
        continue

#%%
df_rooms = fnd.readRooms()
