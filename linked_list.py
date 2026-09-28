class Node:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist, duration):
        newnode = Node(title, artist, duration)

        if self.head is None:
            self.head = newnode
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newnode

        print("\nSong added successfully.")

    def display(self):
        if self.head is None:
            print("\nPlaylist is empty.")
            return

        current = self.head

        print("\n------- Playlist ---------\n")

        while current is not None:
            print("Title     : ", current.title)
            print("Artist    : ", current.artist)
            print("Duration  : ", current.duration)
            print("--------------------------")

            current = current.next

    def remove_song(self, title):
        if self.head is None:
            print("\nPlaylist is empty.")
            return

        # If the song to remove is the first song
        if self.head.title.lower() == title.lower():
            self.head = self.head.next
            print("\nSong removed successfully.")
            return

        current = self.head

        while current.next is not None:
            if current.next.title.lower() == title.lower():
                current.next = current.next.next
                print("\nSong removed successfully.")
                return

            current = current.next

        print("\nSong not found.")

    def play(self, title):
        if self.head is None:
            print("\nPlaylist is empty.")
            return

        current = self.head

        while current is not None:
            if current.title.lower() == title.lower():
                print("\n------- Now Playing -------")
                print("Title     : ", current.title)
                print("Artist    : ", current.artist)
                print("Duration  : ", current.duration)
                return

            current = current.next

        print("\nSong not found.")


playlist = Playlist()

while True:
    print("\n1. Add Song")
    print("2. Display Playlist")
    print("3. Remove Song")
    print("4. Play Song")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
            title = input("Enter song title: ")
            artist = input("Enter artist: ")
            duration = input("Enter duration: ")

            playlist.add_song(title, artist, duration)

    elif choice == 2:
            playlist.display()

    elif choice == 3:
            title = input("Enter song title to remove: ")
            playlist.remove_song(title)

    elif choice == 4:
            title = input("Enter song title to play: ")
            playlist.play(title)

    elif choice == 5:
            print("\nExiting...")
            break

    else:
            print("\nInvalid choice.")

