Fare =500
class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False

    def __str__(self):
        return f"Bus {self.number} | Route: {self.route} | Available Seats: {self.available_seats()}"
    
class Passenger:
    def __init__(self,name,phone,bus):
        self.name=name
        self.phone=phone
        self.bus=bus

class Admin:
    def __init__(self,username="admin",password="1234"):
        self.username=username
        self.password=password

    def login(self):
        uname = input("Enter Admin Username: ")
        pwd = input("Enter Admin Password: ")
        return uname == self.username and pwd == self.password

class BusSystem:
    def __init__(self):
        self.buses=[]
        self.passengers=[]

    def add_bus(self,number,route,seat):
         
        for bus in self.buses:
         if bus.number == number:
          print("Bus with this number already exists.")
          return
        new_bus=Bus(number,route,seat)
        self.buses.append(new_bus)
        print("Bus added successfully.") 

    def show_buses(self):
        if not self.buses:
            print("Not  available.")
        for bus in self.buses:
            print(bus)

    def book_ticket(self,bus_number,name,phone):

        bus= self.find_bus(bus_number)
        if not bus:
            print("Bus not found")
            return

        if bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.passengers.append(passenger)
            print(f" Ticket booked for {name}. and amount is{Fare}")
        else:
            print("No seats available right now in this bus.")

    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None 

def main():
  system = BusSystem()
  admin = Admin()
  logged_in = False

  while True:
        print(" MAIN MENU---")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if admin.login():
                print("Admin login successful.")
                logged_in = True
                while logged_in:
        
                    print("1. Add Bus")
                    print("2. View All Buses")
                    print("3. Logout")
                    adminchoice = input("Enter choice: ")

                    if adminchoice == '1':
                        try:
                            number = input("bus number: ")
                            route = input("bus route: ")
                            seats = int(input("total seats: "))
                            system.add_bus(number, route, seats)
                        except ValueError:
                            print("Invalid seat number.")

                    elif adminchoice == '2':
                        system.show_buses()

                    elif adminchoice == '3':
                        logged_in = False
                        print("Logged out of admin account.")

                    else:
                        print("Invalid option.")
            else:
                print("Username and Password are incorrect.")

        elif choice == '2':

            bus_number = input("bus number: ")
            name = input(" name: ")
            phone = input("phone: ")
            system.book_ticket(bus_number, name, phone)

        elif choice == '3':
            system.show_buses()

        elif choice == '4':
            print("Exiting system!")
            break

        else:
            print("Invalid choice. Please select a valid one.")

if __name__ == "__main__":
    main()




