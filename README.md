# An Instant Room Booking System at the Hertie School

As the final project for the Fall 2021 Data Structures & Algorithms course at the Hertie School, we developed a room booking system that optimizes the assignment of spaces based on individual users' preferences and allows members of the community to receive an instant booking confirmation.

## Background
Under the current system, real-life booking is not possible as each request needs to be manually confirmed by a member of staff. Additionally, students cannot see the capacity of the rooms, nor see all the available, free rooms. Everyone can book a random capacity which leads to inefficient use of space, e.g., there are rooms for 10, booked by 2 students. 

## Features
At the first step, the user is able to either book a room or cancel a room. If the user selects booking a room, they are asked to put in information on themselves and their room booking preferences. Using pandas, our program reads a underlying .csv file into a pandas dataframe, checks for matches between user preferences and room properties, and presents the user with the options, if any. Users can then select the desired room, which will be logged in a bookings file, and receive instant confirmation of their booking. 

Similarly, when cancelling a booking, a function matches the user input with a booking in the booking dataframe and subtracts the indicated number of spaces from the files, instantly opening up more capacity for the next user.

### Using Dataframes for Room Booking
We created two .csv files. One called "Rooms" contains rooms and their unique properties to simulate rooms available at Hertie, and the other one called "Bookings" simulated a booking roster that keeps track of the availability and capacities of a given room at a given time. Since currently there is only a small number of bookable rooms, we generated some mock rooms to simulate more choice and prepare for Hertie's growth trajectory.
 

### Classes
Our program uses different classes for objects, one being "Student" that prompts user input for information such as name, email address, and Student ID. Secondly, the class "Booking Info" creates a  profile based on user input with relevant information about the student's preferences used to match them with an available room, e.g. A/V facilities, quiet study spaces, how many spaces are needed etc. 

### How to Run
The file script.py in the src folder contains the script necessary to run the application, while functions, and classes are saved in and imported from separate files.

### Licensing
This program is free to use under the [MIT License](https://mit-license.org/).

## Authors

[Hannah Schweren](https://github.com/hannahmagda), [Anna Weronika Matysiak](https://github.com/AnnaWeronikaMatysiak), [Max B. Eckert](https://github.com/m-b-e) and [Gabriel da Silva Zech](https://github.com/GabZech).
