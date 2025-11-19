Daily Helper: A Console To-Do List
👋 Hi there!
This project, Daily Helper, is my first attempt at connecting basic programming concepts to a real, everyday need: tracking my own stuff! As a beginner, I kept the design extremely simple—no complex graphics, just pure, functional logic executed in a clean console interface.

📝Project Goal
The primary goal was to create a reliable, console-based application that successfully manages a user's daily to-do list using only fundamental data structures and input/output handling. It serves as a non-distracting digital notepad that won't lose your thoughts.

Domain: Productivity & Automation

Problem Addressed: Reducing mental clutter by providing a fast, reliable place to log and manage tasks.

💡 Concepts Applied from the Course
This project was specifically designed to practice core concepts learned in Introduction to Problem Solving & Programming (or Python/Java Programming fundamentals):

Data Structure (The List): Using a dynamic Python list (tasks = []) to store items, demonstrating how to add, retrieve, and remove elements efficiently.

Control Flow (The Loop): Implementing a central while loop in the run_daily_helper function to continuously display the menu and process user input until the application is explicitly quit.

Modular Programming (Top-Down Design): Breaking the entire application into clear, focused functions (add_task, view_tasks, delete_task) to make the code readable and easy to debug.

I/O and Input Validation: Using the input() function for user interaction and implementing try-except blocks to prevent the program from crashing if a user enters text where a number is expected (e.g., in the delete_task function).
How to Run the Daily Helper
This application requires Python 3 to run.

Save the Code: Ensure the main code is saved as daily_helper.py.

Open Terminal/Command Prompt: Navigate to the project directory where the file is located.

Execute the Script: Run the following command:

Bash
python daily_helper.py

📸 Project Screenshots
The screenshots/ directory contains visual proof of the application running, including:

The main menu screen.
The output after successfully adding a few tasks.
An example of a task being deleted, confirming the functionality.