class Student:
    def __init__(self, name, id, email):
                       self.__name = name
                       self.__id = id
                       self.__email = email
                       
    # functions to get values
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def email(self):
        return self.__email
    
    

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
    
    
    
class bookingInfo:
    
    def __init__(self, places, datetime, quiet, tv, projector):
                       self.__places = places
                       self.__datetime = datetime
                       self.__quiet = quiet
                       self.__tv = tv
                       self.__projector = projector
                       
    # functions to get values
    @property
    def places(self):
        return self.__places
    
    @property
    def datetime(self):
        return self.__datetime
    
    @property
    def quiet(self):
        return self.__quiet
    
    @property
    def tv(self):
        return self.__tv
    
    @property
    def projector(self):
        return self.__projector