# Cinema seat booking system .....
rows = 10
cols = 10

seats = [[0 for i in range(cols)] for j in range(rows)]

def display():
    print(" \n----- Cinema Seats -----")
    print(" \n 0 = Available \n 1 = Booked ")
    for i in range(rows):
        for j in range(cols):
           print(seats[i][j],end=" ")
        print()
        
def Booking():
    r = int(input("\nEnter row to book: "))
    c = int(input("\nEnter column to book: "))
    if r<1 or r>10 or c<1 or c>10:
        print("\nInvalid row or column ")
        return
    if seats[r-1][c-1] == 0:
        seats[r-1][c-1] = 1
        print("\n seat is Booked \n")
    else :
        print("\nseat is already booked.\n")

def cancel():
    r = int(input("\nEnter row to book: "))
    c = int(input("\nEnter column to book: "))
    if r<1 or r>10 or c<1 or c>10:
        print("\nInvalid row or column ")
        return
    if seats[r-1][c-1] == 0:
        print("\n seat is not Booked \n")
    else :
        seats[r-1][c-1] = 0
        print("\nseat is cancelled.\n")

def availability():
    r = int(input("\nEnter row to book (1-10): "))
    c = int(input("\nEnter column to book (1-10): "))
    if r<1 or r>10 or c<1 or c>10:
        print("\nInvalid row or column ")
        return
    if seats[r-1][c-1] == 0:
        print("\n seat is Available \n")
    else :
        print("\nseat is not available.\n")

while(True):
    print("\n1.Display seats")
    print("\n2.Book the seat")
    print("\n3.Check availbility of seat")
    print("\n4.Cancel the seat")
    print("\n5.Exit")
    choice = int(input("\nEnter your choice: "))

    if(choice == 1):
        display()
    elif(choice == 2):
        Booking()
    elif(choice == 3):
        availability()
    elif(choice == 4):
        cancel()
    elif(choice == 5):
        print("Thank You.")
        break
    else:
        print("Enter Valid Choice !")

