# Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
# Requirements:
# - PassengerDetails has name, age.
# - TicketDetails has ticket number, seat number.
# - Booking shows all information.

# Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.

class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def show_details(self):
        print(f"name {self.name}, age {self.age}, ticket_number {self.ticket_number}, seat_number {self.seat_number}")

    
booking = Booking("Krishna", 16, "AI001", 40)
booking.show_details()

