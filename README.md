# An Instant Room Booking System at the Hertie School

As the final project for the Fall 2021 Data Structures & Algorithms course at the Hertie School, we developed a room booking system that optimizes the assignment of spaces based on individual users' preferences and allows members of the community to receive an instant booking confirmation.

## Background
Under the current system, real-life booking is not possible as each request needs to be manually confirmed by a member of staff. Additionally, students cannot see the capacity of the rooms, nor see all the available, free rooms. Everyone can book a random capacity which leads to inefficient use of space, e.g., there are rooms for 10, booked by 2 students. 

## Features
At the first step, the user is able to either book a room or cancel a room. If the user selects booking a room, they are asked to put in information on themselves and their room booking preferences.

### Classes
Our program uses different classes for objects, one being "Student" that prompts user input for information such as name, email address, and Student ID. Secondly, the class "Booking Info" creates a  profile based on user input with relevant information about the student's preferences used to match them with an available room, e.g. A/V facilities, quiet study spaces, how many spaces are needed etc. 

### Using Dataframes for Room Booking
We created a .csv file with rooms and unique properties to simulate rooms at Hertie. Since currently there is only a small number of bookable rooms, we generated some mock rooms.

Our program reads the .csv file into a pandas dataframe, checks for matches between user preferences and room properties, and presents the user with the options, if any. Users can then select the desired room, and receive instant confirmation.  

## Authors

[Hannah Schweren](https://github.com/hannahmagda), [Anna Weronika Matysiak](https://github.com/AnnaWeronikaMatysiak), [Max B. Eckert](https://github.com/m-b-e) and [Gabriel da Silva Zech](https://github.com/GabZech).
