Daily Helper: A Console To-Do List
Hello!
This is the first project, Daily Helper, in which I connect basic programming concepts with a real need: keeping track of my own stuff! As a beginner, I kept the design extremely simple—no complex graphics; pure, functional logic executed in a clean console interface.

Project Goal

The main objective was to implement a robust, console-based application that would successfully manage a user's to-do list for each day, using only the most basic data structures along with input/output handling. It's intended as an undistracting digital notepad that won't misplace your thoughts.

Domain: Productivity & Automation

Problem it solves: Reduces mental clutter by providing a fast, reliable place to log and manage tasks.

Concepts Applied from the Course

This project was specifically designed to practice core concepts learned in Introduction to Problem Solving & Programming (or Python/Java Programming fundamentals):

Data Structure: The List - A dynamic Python list should be used for item storage: tasks = []; also, show how one might efficiently add, retrieve, and remove elements.

Control Flow (The Loop): Utilize a central while loop in the run_daily_helper function to continuously display the menu and process user input until explicitly quit.
Modular ProgrammingTop-Down Design: The division of the whole application into distinct, well-directed functions add_task, view_tasks, and delete_task contributes to code readability and ease of debugging.

I/O and Input Validation: Inputting via the input() function, providing user interaction. Implement try-except blocks to prevent the program from crashing if text is entered by a user where it's expecting a number. For example: in the delete_task() function,


How to Run the Daily Helper

This application requires Python 3 to run.

Save the Code: Make sure the main code is saved as daily_helper.py. 
 Project Screenshots The screenshots/ directory contains visual proof of the application running, including: The main menu screen. The output after adding a few tasks successfully. An example of a task being deleted, confirming functionality.
