class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        self.__hall_list.append(self)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = [[0 for i in range(self.cols)] for i in range(self.rows)]

    def book_seats(self, show_id, rows, cols):
        valid_show_id = False
        for show in self.__show_list:
            if show[0] == show_id:
                valid_show_id = True

        if valid_show_id:
            if rows <= self.rows and cols <= self.cols:
                book_seat = self.__seats[show_id]
                if book_seat[rows - 1][cols - 1] == 0:
                    book_seat[rows - 1][cols - 1] = 1
                    print(f"\n\tSeat: ({rows},{cols}) Booked in Show ID: {show_id}")
                else:
                    print("\n\t-----Seat Already Booked !-----")
            else:
                print("\n\tInvalid Row Or Column Number !")
        else:
            print("\n\t-----Invalid Show ID!-----")

    def view_show_list(self):
        for show in self.__show_list:
            print(f"\nMovie Name: {show[1]}, Show ID: {show[0]}, Time: {show[2]}")

    def view_available_seats(self, show_id):

        valid_show_id = False
        for show in self.__show_list:
            if show[0] == show_id:
                valid_show_id = True

        if valid_show_id:
            print("\n*********** Available Seats ***********")
            for seat in self.__seats[show_id]:
                print(seat)
        else:
            print("\n\t-----Invalid Show ID!-----")


hall = Hall(5, 5, 1)
hall.entry_show(111, "Harry Potter", "19/04/2024 11.00 AM")
hall.entry_show(222, "The Matrix", "19/04/2024 03.00 PM")

while True:
    print("\n1: View All Show Today")
    print("2: Add New Show")
    print("3: View Available Seats")
    print("4: Book Ticket")
    print("5: Exit")
    choice = int(input("\n\tEnter Option: "))

    if choice == 1:
        hall.view_show_list()
    elif choice == 2:
        id = int(input("\n\tEnter Show ID: "))
        name = input("\n\tEnter Movie Name: ")
        time = input("\n\tEnter Show Time: ")
        hall.entry_show(id, name, time)
    elif choice == 3:
        id = int(input("\n\tEnter Show ID: "))
        hall.view_available_seats(id)
    elif choice == 4:
        id = int(input("\n\tEnter Show ID: "))
        ticket_cnt = int(input("\n\tHow Many Ticket: "))
        while ticket_cnt:
            rows = int(input("\n\tEnter Row Number: "))
            cols = int(input("\n\tEnter Cols Number: "))
            hall.book_seats(id, rows, cols)
            ticket_cnt -= 1
    elif choice == 5:
        break
