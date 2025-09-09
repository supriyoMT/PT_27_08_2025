# Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
 
# Requirements:
# -Flight should have attributes: flight number, airline.
# -ScheduledFlight should add departure time and arrival time.
# -Include methods to display complete flight information.
 
 
# Create a base class Person, derived class CraewMember, and a further derived class Pilot.
# -Person contains name and ID.
# -CrewMember adds role (e.g., "Cabin Crew", "Pilot").
# -Pilot adds license number and rank (e.g., "Captain").
 
 
# Create a base class Service, and derive two classes: SecurityService and BaggageService.
# Requirements:
# -Service class has a method service_info().
# -Derived classes override or extend this to describe their own service.
 
 
# Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
# Requirements:
# - PassengerDetails has name, age.
# - TicketDetails has ticket number, seat number.
# - Booking shows all information.

# Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
class Flight:
    def __init__(self,flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline
       
    def show_details(self):
        print(f"flight_number: {self.flight_number}, airline. {self.airline}")

class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, departure_time, arrival_time):
        super().__init__(flight_number, airline)
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def show_flightinfo(self):
        self.show_details()
        print(f"departure_time: {self.departure_time} and arrival_time {self.arrival_time}" )

    
e = ScheduledFlight("I3101", "Air India", "23:10", "07:45")    
e.show_flightinfo()