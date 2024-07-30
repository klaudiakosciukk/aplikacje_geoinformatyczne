class Incident:

    __max_id = 0

    def __init__(self, description, location, priority, time):
        self.id = id
        self.description = description
        self.location = location
        self.priority = priority
        self.time = time
        self.status = 'Undone'
        Incident.__max_id += 1

    def add_ambulance(self, ambulance):
        self.ambulance = ambulance
        ambulance.add_incident(self)
        print(f'Ambulance{self.ambulance.id} was added to incident{self.id}')

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}"