from datetime import datetime

#Samuel Delaney - D00290718 - Student A

class Event:

    def __init__(
            self,
            event_id: int,
            title: str,
            event_type: str,
            date,
            start_time,
            capacity: int,
            venue,
            cancelled: bool,
            ticket_price: float

        ):
        self.event_id = event_id
        self.event_type = event_type
        self.capacity = capacity
        self.date = date
        self.start_time = start_time

        #raise ValueError will crash the program and tell the user a custom error message
        
        # Confirming the capacity is fit for purpose – a capacity cannot be negative

        if self.capacity < 0:
            raise ValueError("Capacity cannot be a negative number.")
        if self.capacity == 0: #There needs to be someone there for the purpose of the event
            raise ValueError("Capacity cannot be 0.")

        # Confirming the venue capacity if fit for purpose – the Venue must hold at least the capacity for this Event.

        if venue.capacity < self.capacity:
            raise ValueError("Event Capacity is too big for the Venue's Capacity")

        # Confirming the event type is an allowable value
        self.allowed_event_types = ["workshop", "open day", "conference", "convention"]
        if self.event_type not in self.allowed_event_types:
            raise ValueError("This event type is not allowed. Allowed event types are: workshop, open day, conference, convention")

    def update_schedule(self):
        date_and_time = datetime.now()
        date = datetime.date(date_and_time) #Get current date
        time = datetime.time(date_and_time) #Get current time
        self.date = date #Redefine the old date to be the new current date
        self.start_time = time #Redefine the old time to be the new current time

    def change_venue(self, new_venue):
        if new_venue.capacity >= self.capacity: #If the new venue has enough space for the capacity
            self.venue = new_venue #Redefine the old venue to be the new venue
            return True
        return False