# Assignment :
 
# Problem Statement

# You are asked to design a Flight Management System in Python using exception handling.
 
# The system should:

# - Read flight information from a file called flights.txt.

# - Each line has: flight_number available_seats price_per_ticket

#   Example: AI101 50 6000
 
# Ask the user for:

# - Flight number

# - Number of tickets to book
 
# Implement the following exception rules: (Questions below)
 
# (a) Raise FlightNotFoundError (custom) if the entered flight number does not exist.
 
# (b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
 
# (c) Handle ValueError if user enters invalid input (like string instead of integer).
 
# (d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket).
 
# (e) Always close the file using finally.
 
# The program should print:

# - Flight details

# - Total booking cost

# - Discount per ticket (total / tickets)
 
# Note**:

# Use nested try-except:
 
# Inner block for booking operations.
 
# Outer block for file handling & re-raised exceptions
 
class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass


try:
    user_flight = input("Please enter the flight number\n")
    reqd_tickets = int(input("Please enter number tickets you want\n"))
    file_path = 'D:\\Coding\\Python\\27ThAug_Training\\VS_Practice\\Exception_handling\\flights.txt'
    with open(file_path, "r") as file:
        try:
            flightFound = False
            avlbl_flightSeats = 0
            avlbl_ticketPrice = 0
            for line in file:
                flt_det = line.strip().split()
                #print(flt_det, flt_det[0], flt_det[1], flt_det[2]) 
                if (flt_det[0] == user_flight):
                    print(f"Flight {user_flight} found\n")
                    flightFound, avlbl_flightSeats, avlbl_ticketPrice = True, int(flt_det[1]), int(flt_det[2])
                    break    
            if (flightFound == False):
                raise FlightNotFoundError(f"Flight {user_flight} not found")
            else:
                if (reqd_tickets > avlbl_flightSeats):
                    raise SeatsUnavailableError("Not enough tickets are available,"
                                                f" user wanted {reqd_tickets}, but only {avlbl_flightSeats} are left," 
                                                "error is SeatsUnavailableError")
            if (flightFound == False):
                raise FlightNotFoundError(f"Flight {user_flight} not found, error is FlightNotFoundError")
            discount = (reqd_tickets * avlbl_ticketPrice) / reqd_tickets
            total = (reqd_tickets * avlbl_ticketPrice) - discount
            print(f"Booked flight {user_flight}, total booking cost {total}, discount {discount}")
        except Exception as e:
            print('An error occurred:', e)     
        finally:
            file.close()    
except ZeroDivisionError as e:
    print('An error of type ZeroDivisionError occurred:', e)
except ValueError as e:
    print('An error of type ValueError occurred:', e)            
except Exception as e:
    print('An error occurred:', e)