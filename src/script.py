import functions as fn
import classes as cl
import pandas as pd
import datetime

'''
TO-DOs

- Create more day and hour entries for every room on the excel file (currently only for 01.01.2022 and 10pm)


'''

# %%


# create rooms
# room1=Room("2.31", 2, True, True, False)
# room2=Room("2.32", 3, True, False, False)
# room3=Room("2.35", 8, False, False, False)
# room4=Room("2.40", 2, True, True, False)
# room5=Room("3.60", 4, True, False, True)
# room6=Room("2.71", 4, False, False, False)
# room7=Room("3.01", 35, False, True, False)
# room8=Room("3.10", 7, False, True, False)
# room9=Room("3.22", 3, True, False, False)
# room10=Room("3.33", 5, True, False, False)
# room11=Room("3.35", 12, True, False, True)
# room12=Room("3.40", 15, False, True, True)
# room13=Room("3.50", 17, False, False, False)
# room14=Room("3.60", 4, True, False, False)



#%%

new_student = cl.Student(fn.askStudentName(), fn.askStudentID(), fn.askStudentEmail())


#%%

# import dataframe of rooms
df = pd.read_excel("../data/raw/rooms.xlsx", dtype={"name": str})

# given user input, create object with all matching available rooms

# user input
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

def chooseRoom(df):
    
    num_avl_rooms = df.shape[0] # number of rows = number of available rooms
    room_names_list = df['name'].tolist()
    room_names_string = "\n".join(map(str, room_names_list))
    
    print(f"There are {num_avl_rooms} available rooms:\n{room_names_string}")
    
    while True:
        chosen_room = input("Which would you like to book? ")
      
        if chosen_room not in room_names_list: 
            print("Error. Please provide a valid room number.")
        else:
            return chosen_room


chooseRoom(df_match)

# def roomsToObjects(df):
#     for row in df:
#         name = df.name
#         quiet = df.quiet
#         tv = df.tv
#         projector = df.projector
#         day = day(df.date_time)
#         time = hour(df.date_time)
#         available_spaces = df.available_spaces
        
# roomsToObjects(df_match)
#desired_room = cl.Room(1, True, False, False)

#%%

print(df_match.shape[0])
room_names = df_match['name'].tolist()

#print(f"a {(*room_names, sep=', ')}")
string = "\n".join(map(str, room_names))
print(string)

# after confirmation update dataframe with informations from user

