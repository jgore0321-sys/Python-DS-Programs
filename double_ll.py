# Assignment 4: Doubly Linked List - Text Editor

class Node:
    def __init__(self, text):
        self.text = text
        self.prev = None
        self.next = None


class TextEditor:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert text at the end
    def insert_text(self, text):
        new_node = Node(text)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        print("Text inserted successfully.")

    # Delete text
    def delete_text(self, text):
        current = self.head

        while current is not None:
            if current.text.lower() == text.lower():

                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                print("Text deleted successfully.")
                return

            current = current.next

        print("Text not found.")

    # Display text from beginning to end
    def display_text(self):
        if self.head is None:
            print("Text buffer is empty.")
            return

        current = self.head
        print("\nText:")

        while current is not None:
            print(current.text, end=" ")
            current = current.next

        print()

    # Search text
    def search_text(self, text):
        current = self.head

        while current is not None:
            if current.text.lower() == text.lower():
                print("Text found.")
                return

            current = current.next

        print("Text not found.")

    # Display text in reverse
    def display_reverse(self):
        if self.tail is None:
            print("Text buffer is empty.")
            return

        current = self.tail
        print("\nText in Reverse:")

        while current is not None:
            print(current.text, end=" ")
            current = current.prev

        print()


editor = TextEditor()

while True:
    print("\n===== DOUBLY LINKED LIST TEXT EDITOR =====")
    print("1. Insert Text")
    print("2. Delete Text")
    print("3. Display Text")
    print("4. Search Text")
    print("5. Print Text in Reverse")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text to insert: ")
        editor.insert_text(text)

    elif choice == "2":
        text = input("Enter text to delete: ")
        editor.delete_text(text)

    elif choice == "3":
        editor.display_text()

    elif choice == "4":
        text = input("Enter text to search: ")
        editor.search_text(text)

    elif choice == "5":
        editor.display_reverse()

    elif choice == "6":
        print("Exiting Text Editor. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")