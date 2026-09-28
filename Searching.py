students = [
    {"Roll": 1, "Name": "Aman", "SGPA": 8.65},
    {"Roll": 2, "Name": "Raj", "SGPA": 8.12},
    {"Roll": 3, "Name": "Jai", "SGPA": 9.00},
    {"Roll": 4, "Name": "Om", "SGPA": 8.92},
    {"Roll": 5, "Name": "Sai", "SGPA": 9.65},
    {"Roll": 6, "Name": "Ravi", "SGPA": 9.35},
    {"Roll": 7, "Name": "Ajai", "SGPA": 9.34},
    {"Roll": 8, "Name": "Amar", "SGPA": 7.63},
    {"Roll": 9, "Name": "Ritesh", "SGPA": 9.30},
    {"Roll": 10, "Name": "Kishor", "SGPA": 9.67},
    {"Roll": 11, "Name": "Hari", "SGPA": 6.89},
    {"Roll": 12, "Name": "Harshad", "SGPA": 9.98},
    {"Roll": 13, "Name": "Amay", "SGPA": 9.00},
    {"Roll": 14, "Name": "Mangesh", "SGPA": 8.12},
    {"Roll": 15, "Name": "Ram", "SGPA": 8.00}
]

target = 9.00


def linear_search():
    Found = False

    for i in students:
        if i["SGPA"] == target:
            print("------ Student Found ------")
            print("Name :", i["Name"])
            print("Roll :", i["Roll"])
            print("SGPA :", i["SGPA"])
            print()
            Found = True

    if not Found:
        print("----- Student Not Found -----")


def binary_search():
    Found = False

    students.sort(key=lambda x: x["SGPA"])

    print("\n---------SORTED STUDENT DATA------------")
    for student in students:
        print(student)

    low = 0
    high = len(students) - 1

    while low <= high:
        mid = (low + high) // 2

        if students[mid]["SGPA"] == target:
            Found = True
            break

        elif students[mid]["SGPA"] < target:
            low = mid + 1

        else:
            high = mid - 1

    if Found:
        print("\nStudents with SGPA 9.00: ")

        for student in students:
            if student["SGPA"] == target:
                print("Name : ", student["Name"])
                print("Roll : ", student["Roll"])
                print("SGPA : ", student["SGPA"])
                print()

    else:
        print("\nNo student found with SGPA 9.00")


Method = input("Enter Method for Searching (Binary(B) or Linear(L)): ").upper()

if Method == 'B':
    binary_search()

elif Method == 'L':
    linear_search()

else:
    print("\nInvalid Input!")