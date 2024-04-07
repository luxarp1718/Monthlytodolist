#Monthly todo list
    #### Video Demo:  <https://youtu.be/A3wM1LC0OQI>
    #### Description:
    #Monthly TODO list

    Monthly Todo list is a simple to-do list application that helps you organize your tasks according to the date.

    #Features
    - Add a number of tasks at once.
    - Each task can be set its own date of completion.
    - Shows tasks of the requested month in a user friendly format.

    #WALKTHROUGH

    To find the function of my project took quite a long time. However, after I figured that out, I started working on it non stop. Firstly, I tried designing a pseudocode which made the programming process look simple, but once I started it, a ton of changes had to be made in it. I wanted to include almost evertything I learned from the CS50P course.

    I started the main programming by first seperating the different functions of command line arguments such as add and view. Then I coded the part of adding the task and the date along with it. I used a class called "Create" to add the task of the user with its corresponding date into an array called "tasks" as a dictionary. The use of class was not completely necessary, but I wanted to get familiar with using object oriented porgramming, so I thought of including it.

    I defined another function named "add_to_file" to add the task and date into a file called "tasks.txt" so that i can be read by the program later. All the verification of the date and tasks were done in the class "Create" itself. The data were written on the file in a csv format using dictionary so "csv.Dictwiter" was also used in the function.

    Once the adding part was done, I coded the part of viewing the task. For this, the input of the user was verified using "re.search". Another function named "get_from_file" was used to retrieve required data from the file created before as a dictionary. This function evaluated the date the user had entered with the dates in the file to append the appropriate task and its date into an array named "to_return". Library function "date" was used to set the type to date. "calendar" function was also used to iter through the days of the month provided by the user. The month number was obtained from a defined function called "get_month_num". To add more user friendliness, I defined another function named "get_month_name" to return the name of the month so that the user can understand the output with a light mind.

    After the array was returned to the main fucntion, it printed out the datas in a "rounded_grid" format using "tabulate".

    Messages like "Cannot access past tasks" will also be output if the user does not provide suitable inputs.

    These all are in a single python file called "project.py". Test of the functions in this file are in "test_project.py", which uses "pytest" as well as "date" functions to test the project. All the pip installed libraries are in "requirements.txt" in the specified format.

    Overall, the making of this project was quite overwhelming at beginning but it turned out to be satisfying at the end. It is certainly one of my great achievements.




