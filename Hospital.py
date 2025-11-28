import os
import sys
import pickle
from dataclasses import dataclass, field

@dataclass
class Patient:
    id: int
    name: str
    age: int
    problem: str

@dataclass
class Doctor:
    id: int
    name: str
    department: str
    specialization: str

@dataclass
class Worker:
    id: int
    name: str
    task: str
    shift: str

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.workers = []
        self.load_data()
        self.current_id = {
            'patient': len(self.patients) + 1,
            'doctor': len(self.doctors) + 1,
            'worker': len(self.workers) + 1
        }

    def load_data(self):
        if os.path.exists("Hospitaldata.pkl"):
            with open("Hospitaldata.pkl", "rb") as file:
                data = pickle.load(file)
                self.patients = data.get('patients', [])
                self.doctors = data.get('doctors', [])
                self.workers = data.get('workers', [])
        else:
            self.patients, self.doctors, self.workers = [], [], []

    def save_data(self):
        with open("Hospitaldata.pkl", "wb") as file:
            pickle.dump({
                'patients': self.patients,
                'doctors': self.doctors,
                'workers': self.workers
            }, file)

    def register_patient(self):
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        problem = input("Enter patient's problem: ")
        patient = Patient(self.current_id['patient'], name, age, problem)
        self.patients.append(patient)
        self.current_id['patient'] += 1
        self.save_data()
        print("Patient registered successfully.")

    def register_doctor(self):
        name = input("Enter doctor's name: ")
        department = input("Enter doctor's department: ")
        specialization = input("Enter doctor's specialization: ")
        doctor = Doctor(self.current_id['doctor'], name, department, specialization)
        self.doctors.append(doctor)
        self.current_id['doctor'] += 1
        self.save_data()
        print("Doctor registered successfully.")

    def register_worker(self):
        name = input("Enter worker's name: ")
        task = input("Enter worker's task: ")
        shift = input("Enter worker's shift: ")
        worker = Worker(self.current_id['worker'], name, task, shift)
        self.workers.append(worker)
        self.current_id['worker'] += 1
        self.save_data()
        print("Worker registered successfully.")

    def view_patients(self):
        print("Patients List:")
        for patient in self.patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Problem: {patient.problem}")
        print(f"Total Patients: {len(self.patients)}")

    def view_doctors(self):
        print("Doctors List:")
        for doctor in self.doctors:
            print(f"ID: {doctor.id}, Name: {doctor.name}, Department: {doctor.department}, Specialization: {doctor.specialization}")
        print(f"Total Doctors: {len(self.doctors)}")

    def view_workers(self):
        print("Workers List:")
        for worker in self.workers:
            print(f"ID: {worker.id}, Name: {worker.name}, Task: {worker.task}, Shift: {worker.shift}")
        print(f"Total Workers: {len(self.workers)}")

    def search_by_id(self):
        category = input("Enter category (patient/doctor/worker): ").lower()
        record_id = int(input("Enter ID: "))
        if category == 'patient':
            record = next((p for p in self.patients if p.id == record_id), None)
        elif category == 'doctor':
            record = next((d for d in self.doctors if d.id == record_id), None)
        elif category == 'worker':
            record = next((w for w in self.workers if w.id == record_id), None)
        else:
            print("Invalid category.")
            return
        if record:
            print(record)
        else:
            print("Record not found.")

    def update_record(self):
        category = input("Enter category (patient/doctor/worker): ").lower()
        record_id = int(input("Enter ID: "))
        if category == 'patient':
            record = next((p for p in self.patients if p.id == record_id), None)
            if record:
                field_to_update = input("Enter field to update (name/age/problem): ").lower()
                if field_to_update == 'name':
                    record.name = input("Enter new name: ")
                elif field_to_update == 'age':
                    record.age = int(input("Enter new age: "))
                elif field_to_update == 'problem':
                    record.problem = input("Enter new problem: ")
                else:
                    print("Invalid field.")
                    return
                self.save_data()
                print("Record updated successfully.")
            else:
                print("Record not found.")
        elif category == 'doctor':
            record = next((d for d in self.doctors if d.id == record_id), None)
            if record:
                field_to_update = input("Enter field to update (name/department/specialization): ").lower()
                if field_to_update == 'name':
                    record.name = input("Enter new name: ")
                elif field_to_update == 'department':
                    record.department = input("Enter new department: ")
                elif field_to_update == 'specialization':
                    record.specialization = input("Enter new specialization: ")
                else:
                    print("Invalid field.")
                    return
                self.save_data()
                print("Record updated successfully.")
            else:
                print("Record not found.")
        elif category == 'worker':
            record = next((w for w in self.workers if w.id == record_id), None)
            if record:
                field_to_update = input("Enter field to update (name/task/shift): ").lower()
                if field_to_update == 'name':
                    record.name = input("Enter new name: ")
                elif field_to_update == 'task':
                    record.task = input("Enter new task: ")
                elif field_to_update == 'shift':
                    record.shift = input("Enter new shift: ")
                else:
                    print("Invalid field.")
                    return
                self.save_data()
                print("Record updated successfully.")
            else:
                print("Record not found.")
        else:
            print("Invalid category.")

    def delete_record(self):
        category = input("Enter category (patient/doctor/worker): ").lower()
        record_id = int(input("Enter ID: "))
        if category == 'patient':
            self.patients = [p for p in self.patients if p.id != record_id]
            self.save_data()
            print("Record deleted successfully.")
        elif category == 'doctor':
            self.doctors = [d for d in self.doctors if d.id != record_id]
            self.save_data()
            print("Record deleted successfully.")
        elif category == 'worker':
            self.workers = [w for w in self.workers if w.id != record_id]
            self.save_data()
            print("Record deleted successfully.")
        else:
            print("Invalid category.")

    def main_menu(self):
        while True:
            print("\n--- Hospital Management System ---")
            print("1. Register Patient")
            print("2. Register Doctor")
            print("3. Register Worker")
            print("4. View all Patients")
            print("5. View all Doctors")
            print("6. View all Workers")
            print("7. Search by ID")
            print("8. Update/Delete records by ID")
            print("9. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.register_patient()
            elif choice == '2':
                self.register_doctor()
            elif choice == '3':
                self.register_worker()
            elif choice == '4':
                self.view_patients()
            elif choice == '5':
                self.view_doctors()
            elif choice == '6':
                self.view_workers()
            elif choice == '7':
                self.search_by_id()
            elif choice == '8':
                action = input("Do you want to update or delete? (update/delete): ").lower()
                if action == 'update':
                    self.update_record()
                elif action == 'delete':
                    self.delete_record()
                else:
                    print("Invalid action.")
            elif choice == '9':
                print("Exiting the system.")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "hospital123":
        print("Login successful.")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

if __name__ == "__main__":
    if login():
        hms = HospitalManagementSystem()
        hms.main_menu()
