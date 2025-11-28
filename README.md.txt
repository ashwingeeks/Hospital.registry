Hospital Management System (CLI, Python)
This project constitutes a simple command-line-based Hospital Management System and is written in Python. It allows the administrator to manage Patients, Doctors, and Workers with basic CRUD operations like create, read, update, and delete. It stores all data persistently using Python's pickle module so that records remain available between runs of the program. ​​
Features
Secure login via username/password for access control
Register:
Patients (name, age, problem)
Doctors: Names, Departments, Specializations
Workers (name, task, shift)
View all records for each category
Search records individually by ID (patient/doctor/worker)
Update fields of an existing record: name, problem, department, task, etc.
Delete records by ID for any category
Persistent storage in a single binary file: Hospitaldata.pkl
Technologies Used
Python 3.x​
Standard Library:
dataclasses, для определения Patient, Doctor, Worker ​​​
pickle (for simple file-based persistence)
os, sys (for file handling and clean exit)
How It Works
Data Classes:
Patient: id, name, age, problem
Doctor: id, name, department, specialization
Worker: id, name, task, shift
The class HospitalManagementSystem:
Upon startup, it loads data from Hospitaldata.pkl if it does exist; otherwise, it starts with empty lists.
Maintains separate lists for patients, doctors, and workers.
keep track of the next ID to assign for each category, using a simple counter.

Main operations:
Register functions: it creates the instances of dataclasses, appends to lists and saves to file.
View functions - view_patients, view_doctors, view_workers, print all records along with totals.
search_by_id: Finds a record by ID in a selected category and prints it.
update_record finds a record and allows the user to edit certain fields.
delete_record removes a record with the given ID and rewrites the data stored.
Login:
The login() function requests a username and password when the program is started.
Default credentials are:
Username: admin
Password: hospital123

How to Run
Ensure Python 3 is installed on your system.​
Save the code in a file, for instance :
HospitalManagementSystem.py
Open the terminal or commad prompt in the folder where the file is located.
Run the following:
On Windows:
python HospitalManagementSystem.py
On macOS/Linux:
python3 HospitalManagementSystem.py
Enter the login credentials when prompted.
Perform operations using the numeric main menu:
1–3: Register patient/doctor/worker
4–6: Display all records for each category
7: Search by ID
8: Update or delete a record by ID
9: Quit the application
A binary data file named Hospitaldata.pkl will be automatically created in the same directory. This will store all records.​

File Structure
HospitalManagementSystem.py – main application script
hospitaldata.pkl – auto-created data file storing all records (patients, doctors, workers)
Notes and Limitations This is just a simple console application with a menu that is text-based; no GUI is present. Only one admin user is supported, and the username and password are hard-coded. No advanced search is available, such as by name or department; search is strictly by numeric ID. Data is stored in one single pickle file; no relational database is used. ​​ Possible Future Improvements Add input validation for empty strings and enhanced error messages.​ Implement search by name, department, or problem. Add role-based access control: different logins for doctors/staff. Replace pickle with a database (SQLite/MySQL) for scalability/safer persistence.​​ Create a graphical user interface using Tkinter or a web interface using Flask/Django.​
