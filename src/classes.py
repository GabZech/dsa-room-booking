class Student:
     def __init__(self, name, id, email):
                       self.__name = name
                       self.__id = id
                       self.__email = email

## create getters for Student name, id and email

class Room:

    def __init__(self, capacity, quiet, tv, projector):
        self.__capacity = capacity
        self.__quiet = quiet 
        self.__tv = tv
        self.__projector = projector
    
    
    # function to get value of __capacity
    @property
    def capacity(self):
        return self.__capacity
      
    # function to set value of __capacity
    @capacity.setter
    def capacity(self, c):
        self.__capacity = c
    
