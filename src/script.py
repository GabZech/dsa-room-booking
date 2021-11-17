import functions as fn
import classes as cl
import pandas as pd
import openpyxl

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

df = pd.read_excel("../data/raw/rooms.xlsx")

# given user input, create object with all matching available rooms

des_capacity = 1
des_quiet = True
des_tv = False
des_projector = False

desired_room = cl.Room(1, True, False, False)

print(desired_room.capacity)

# after confirmation update dataframe with informations from user

