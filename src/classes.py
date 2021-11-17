class Student:
     def __init__(self, name, id, email):
                       self._name = name
                       self._id = id
                       self._email = email

## create getters for Student name, id and email

class Room:

    def __init__(self, name, capacity, quiet, tv, projector):
        self.__name = name
        self.__capacity = capacity
        self.__quiet = quiet 
        self.__tv = tv
        self.__projector = projector