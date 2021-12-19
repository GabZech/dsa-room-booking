class Student:

    '''
    The class Student is used to store information about student's booking preferences.
    
    Arributes:
    ----------
        name: str
            the name of the Student
        id: int 
            the ID of the student
        email:str
            The email of the student
    
    Methods:
    ----------
    None
    
    '''

    def __init__(self, name, id, email):
        
        '''
        Parameters:
        ----------
        name: str
            the name of the Student
        id: int 
            the ID of the student
        email:str
            The email of the student
        
        '''
        
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
    
    '''
    The class Student is used to store information about student's booking preferences.
    
    Arributes:
    ----------
    capacity: str
        the capacity of a room
    quiet: int 
        whether or not room is a quiet study space
    tv:str
        whether or not room has a TV
    projector: str
        whether or not room has a projector
    
    Methods:
    ----------
    none
    
    '''

    def __init__(self, capacity, quiet, tv, projector):
        
        '''
        Parameters:
        ----------
       capacity: str
           the capacity of a room
       quiet: int 
           whether or not room is a quiet study space
       tv:str
           whether or not room has a TV
       projector: str
           whether or not room has a projector
    
        '''
        
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

    '''
    The class bookingInfo is used to store information about a booking.
    
    Attributes:
    ---------- 
    places: int
        the number of places booked.
    datetime: datetime.datetime
        the date and time of the booking.
    quiet: bool
        whether the booking is for a quiet room.
    tv: bool
        whether the booking needs a TV.
    projector:bool
        whether the booking needs a projector.
        
    Methods
    -------
    None
    
    '''
    
    def __init__(self, places, datetime, quiet, tv, projector):
        
        '''
        The class bookingInfo is used to store information about a booking.
        
        Attributes:
        ---------- 
        places: int
            the number of places booked.
        datetime: datetime
            the date and time of the booking in date in mm/dd/YY, hh format.
        quiet: bool
            whether the booking is for a quiet room.
        tv: bool
            whether the booking needs a TV.
        projector:bool
            whether the booking needs a projector.
        
        '''
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
    
