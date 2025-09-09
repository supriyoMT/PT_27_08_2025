# Create a base class Person, derived class CraewMember, and a further derived class Pilot.
# -Person contains name and ID.
# -CrewMember adds role (e.g., "Cabin Crew", "Pilot").
# -Pilot adds license number and rank (e.g., "Captain").


class Person:
    def __init__(self,name, ID):
        self.name = name
        self.ID = ID
       
    def show_details(self):
        print(f"name: {self.name}, ID. {self.ID}")

class CraewMember(Person):
    def __init__(self, name, ID, role):
        super().__init__(name, ID)
        self.role = role

    def show_crewinfo(self):
        self.show_details()
        print(f"role {self.role}" )


class Pilot(CraewMember):
    def __init__(self, name, ID, role, license_number, rank):
        super().__init__(name, ID, role)
        self.license_number = license_number
        self.rank = rank

    def show_pilotinfo(self):
        self.show_details()
        self.show_crewinfo()
        print(f"license_number {self.license_number}, rank {self.rank}" )
    

pilot = Pilot("Pilot1", "P001", "Pilot", "LIC_001", "Captain")
pilot.show_pilotinfo()