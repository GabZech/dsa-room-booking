import functions as fn
import classes as cl
import datetime
import time

'''
TO-DOs
1) URGENT:

 a) name: more than one letter
 b) capacity: add condition, but in the script unless we set a max value as constant
    #if places> df_rooms["capacity"].max():
    #print:("Hertie is super small, be realistic, pick smaller number")
    
c) time: We do not need minutes in df_rooms;
    as we only can book for an hour and only starting from full hours, 
    shall we maybe let them only pick the hour without minutes?
    

d) I belive we should get rid of chose room function and cancel booking function. 
   They are overlaping to some extent with script and also, maybe it would be more efficient
   to have them in one place in script. Issues that are problematic here:
       - when you cancel a room and you are later asked what you want to do, and clik again 
       cancel, the room that you selected will still be there, at least the first time you select
       it
       -when there is only one room, program still asks "which room you want to select"
       
5) booking a room - it would be good to compare exisitng names and id in df_bookings while inputing names and ID. 
   Gabriel set his studnet number as 123456 so did I. While cancelling I also cancelled 
   his whithout knowing.
       
2) ADDITIONAL and USEFUL:
- Allow users to choose 1 or 2h for booking a room
- Show how many spaces available per room
- set a timer between booking and showing options
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
                                 datetime = fn.askbookingInfoTime())
        


        # find matching rooms
        df_match = df_rooms[(df_rooms.date_time == booking.datetime) &
                            (df_rooms.available_places >= booking.places) & # return rooms with same or higher number of availabe places
                            (df_rooms.quiet == booking.quiet) &
                            (df_rooms.tv == booking.tv) &
                            (df_rooms.projector == booking.projector)
                            ]
        
        # choose room
        chosen_room_index, chosen_room_name = fn.chooseRoom(df_match)
        
        if len(df_match)==0:
            print("We are sorry, there are no rooms with such criterias, please try again later")
            break
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
