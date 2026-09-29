queue = []
token = 1

def enqueue():
    global token
    name = input("Enter Customer Name : ")
    queue.append((token,name))
    print("Token: ",token,"assigned to: ",name)
    token+=1

def dequeue():
    if not queue:
        print("No customer is waiting.")
    else:
        token,name = queue.pop(0)
        print("Serving Customer: ")
        print("Token: ",token)
        print("Name: ",name)

def display():
    if not queue:
        print("No customer is waiting.")
    else:
        print("\nWaiting Customer: ")
        for token,name in queue:
            print("Token: ",token,"|| Name: ",name)

while(True):
    print("\n---------- Bank Token Queue ----------\n")
    print("1.New Customer")
    print("2.Serve Customer")
    print("3.Display Waiting Customer")
    print("4.Exit")

    choice = int(input("Enter Your Choice: "))

    if(choice == 1):
        enqueue()
    elif(choice == 2):
        dequeue()
    elif(choice == 3):
        display()
    elif(choice == 4):
        print("Exiting...")
        break
    else:
        print("Invalid Choice Input!")