from fleet.ambulance import Ambulance
from operations import *
from personnel import *
from fleet.ambulance import Ambulance
from fleet.station import Station
from random import randint 

def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
   # incident1 = Incident(1, "Power outage in sector 4")
   # incident2 = Incident(2, "Fire alarm in building 21")
   # queue += incident1
   # queue += incident2

    # wypisz wszystkie zgłoszenia
    #print("Aktualne zgłoszenia:")
    #print(queue)

    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

     # Zaraportowanie 2 zgłoszeń
    # Generowanie losowego priorytetu
    priority1 = randint(1, 10)
    priority2 = randint(1, 10)
  
    incident1 = Incident("Power outage in sector 4", (51, 20), priority1, "12:00")
    incident2 = Incident("Fire alarm in building 21", (50, 20), priority2, "13:00")

    queue += incident1
    queue += incident2

    print("Aktualne zgłoszenia:")
    print(queue)
    
    station1 = Station((50.5, 18.5), ambulance1, driver1, employee1)
    print(f'Station one: {station1}')
   

    incident1.add_ambulance(ambulance1)  
    incident2.add_ambulance(ambulance1) 
    assert queue[0].ambulance is not None
    assert ambulance1.incident is not None

    ambulance1.ambulancee()


    # Sprawdzenie czy wszystkie incydenty zostały zakończone
    for incident in queue:
        assert incident.status == "done"



if __name__ == "__main__":
    run_application()