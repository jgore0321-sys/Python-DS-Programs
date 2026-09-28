employees = [
    {"EMP-ID": 105, "EMP-Name": "Ravi", "EMP-Salary": 45000},
    {"EMP-ID": 102, "EMP-Name": "Aman", "EMP-Salary": 35000},
    {"EMP-ID": 108, "EMP-Name": "Jay", "EMP-Salary": 50000},
    {"EMP-ID": 101, "EMP-Name": "Om", "EMP-Salary": 30000},
    {"EMP-ID": 104, "EMP-Name": "Raj", "EMP-Salary": 40000}
]

def quick_sort(arr, low, high):

    if low < high:

        pivot = arr[low]["EMP-ID"]

        i = low + 1
        j = high

        while i <= j:

            while i <= high and arr[i]["EMP-ID"] <= pivot:
                i += 1

            while j >= low and arr[j]["EMP-ID"] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        p = j

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i]["EMP-Name"] < right[j]["EMP-Name"]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def display(arr):
    for employee in arr:
        print(employee)


print("Original Employee Data:")
display(employees)

choice = int(input("Enter type of sorting to execute (Quick sort(1) and Merge sort(2)): "))

if choice == 1:
    quick_sort(employees, 0, len(employees) - 1)

    print("\nEmployees sorted by EMP-ID:")
    display(employees)

elif choice == 2:
    employees = merge_sort(employees)

    print("\nEmployees sorted alphabetically by EMP-Name:")
    display(employees)
    
else:
    print("Invalid Input!")