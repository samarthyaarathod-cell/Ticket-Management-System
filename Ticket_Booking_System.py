# Ticket Booking System using
# Array, Queue, Stack and Searching

from collections import deque


# --------- Ticket Class ---------
class Ticket:
    def __init__(self, seat_no, name):
        self.seat_no = seat_no
        self.name = name


# --------- Ticket System ---------
class TicketSystem:

    def __init__(self, total_seats=10):
        self.total_seats = total_seats
        self.seats = [None] * total_seats     # Array for seats
        self.waiting_queue = deque()          # Queue for waiting list
        self.cancel_stack = []                # Stack for cancellation history


    # --------- Book Tickets ---------
    def book_ticket(self):

        n = int(input("How many tickets you want to book: "))

        for i in range(n):

            print(f"\nEnter details for Ticket {i+1}")
            name = input("Enter customer name: ")

            booked = False

            for j in range(self.total_seats):

                if self.seats[j] is None:

                    ticket = Ticket(j+1, name)
                    self.seats[j] = ticket

                    print(f"Ticket booked successfully! Seat No: {j+1}")
                    booked = True
                    break

            if not booked:

                print("No seats available!")

                choice = input("Add to waiting list? (y/n): ")

                if choice.lower() == 'y':
                    self.waiting_queue.append(name)
                    print("Added to waiting list.")


    # --------- Cancel Ticket ---------
    def cancel_ticket(self):

        seat_no = int(input("Enter seat number to cancel: "))

        if seat_no < 1 or seat_no > self.total_seats:
            print("Invalid seat number!")
            return

        if self.seats[seat_no-1] is None:
            print("Seat already empty!")
            return

        ticket = self.seats[seat_no-1]
        self.seats[seat_no-1] = None
        self.cancel_stack.append(ticket)

        print("Ticket cancelled successfully!")

        # Check waiting list
        if self.waiting_queue:

            name = self.waiting_queue.popleft()
            new_ticket = Ticket(seat_no, name)
            self.seats[seat_no-1] = new_ticket

            print(f"Seat given to waiting customer: {name}")


    # --------- Show Available Seats ---------
    def show_available_seats(self):

        print("\nSeat Status")

        for i in range(self.total_seats):

            if self.seats[i] is None:
                print(f"Seat {i+1} : Available")
            else:
                print(f"Seat {i+1} : Booked by {self.seats[i].name}")


    # --------- Search Booking ---------
    def search_booking(self):

        name = input("Enter customer name to search: ")

        for ticket in self.seats:

            if ticket and ticket.name.lower() == name.lower():

                print("\nBooking Found")
                print("Name:", ticket.name)
                print("Seat Number:", ticket.seat_no)
                return

        print("Booking not found!")


    # --------- Show Waiting List ---------
    def show_waiting_list(self):

        if not self.waiting_queue:
            print("Waiting list empty.")
            return

        print("\nWaiting List")

        for person in self.waiting_queue:
            print(person)


    # --------- Show Cancellation History ---------
    def show_cancellations(self):

        if not self.cancel_stack:
            print("No cancellations yet.")
            return

        print("\nCancellation History")

        for ticket in reversed(self.cancel_stack):
            print(ticket.name, "- Seat", ticket.seat_no)


# --------- Main Program ---------
def main():

    system = TicketSystem()

    while True:

        print("\n===== Ticket Booking System =====")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Show Available Seats")
        print("4. Search Booking")
        print("5. Waiting List")
        print("6. Cancellation History")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            system.book_ticket()

        elif choice == 2:
            system.cancel_ticket()

        elif choice == 3:
            system.show_available_seats()

        elif choice == 4:
            system.search_booking()

        elif choice == 5:
            system.show_waiting_list()

        elif choice == 6:
            system.show_cancellations()

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()