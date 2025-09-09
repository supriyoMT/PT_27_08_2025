# Create a base class Service, and derive two classes: SecurityService and BaggageService.
# Requirements:
# -Service class has a method service_info().
# -Derived classes override or extend this to describe their own service.

class Service:
    def service_info(self):
        print("This is service_info from Service")


class SecurityService(Service):
    def service_info(self):
        print("This is SecurityService overriden from Service")

class BaggageService(Service):
    def service_info(self):
        print("This is BaggageService overriden from Service")      

service = Service()
service.service_info()

secService = SecurityService()  
secService.service_info()

bagService = BaggageService()  
bagService.service_info()