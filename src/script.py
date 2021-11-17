import functions as fn
import classes as cl

# %%


# create rooms
room1=Room("2.31", 2, True, True, False)
room2=Room("2.32", 3, True, False, False)
room3=Room("2.35", 8, False, False, False)
room4=Room("2.31", 2, True, True, False)
room5=Room("3.22", 4, True, False, True)
room6=Room("3.47", 4, False, False, False)
room7=Room("2.71", 7, False, True, False)
room8=Room("3.10", 7, False, True, False)
room9=Room("2.32", 3, True, False, False)
room10=Room("3.33", 5, True, False, False)
room11=Room("3.35", 12, True, False, True)
room12=Room("3.40", 15, False, True, True)
room13=Room("3.50", 17, False, False, False)
room14=Room("3.60", 4, True, False, False)

# %%


#%%

new_student = cl.Student(fn.askStudentName(), fn.askStudentID(), fn.askStudentEmail())

