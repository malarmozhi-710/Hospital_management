import csv

file_path = r"C:\Users\malar\Downloads\Patient(1).csv"

# Add Patient
with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["101", "Ravi", "30", "Fever"])
    writer.writerow(["102", "Anu", "25", "Cold"])

print("Patients Added\n")

# View Patients
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\nUpdating Patient...\n")

# Update Patient (Example: ID = 101)
rows = []
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "101":
            row = ["101", "Ravi", "31", "Flu"]   # Updated data
        rows.append(row)

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# View after update
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\nDeleting Patient...\n")

# Delete Patient (Example: ID = 102)
rows = []
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != "102":
            rows.append(row)

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Final View
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)