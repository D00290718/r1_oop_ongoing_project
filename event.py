from venue import Venue
import datetime

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
            venue: Venue,
            cancelled: bool,
            ticket_price: float

        ):
        self.event_id = event_id
        self.event_type = event_type
        self.capacity = capacity
        self.date = date
        self.start_time = start_time
        self.cancelled = cancelled

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
        date_and_time = datetime.datetime.now()
        date = datetime.datetime.date(date_and_time) #Get current date
        time = datetime.datetime.time(date_and_time) #Get current time
        self.date = date #Redefine the old date to be the new current date
        self.start_time = time #Redefine the old time to be the new current time

    def change_venue(self, new_venue):
        if new_venue.capacity >= self.capacity: #If the new venue has enough space for the capacity
            self.venue = new_venue #Redefine the old venue to be the new venue
            return True
        return False

    def change_type(self, new_event_type):
        if new_event_type in self.allowed_event_types:
            #The new event type is allowed so now redefine the event type to be the new one
            self.event_type = new_event_type
            return True
        #The new event type is not one of the valid options so just return False and don't change anything
        return False
    
    def cancel_event(self):
        current_date_and_time = datetime.datetime.now()
        current_date = datetime.datetime.date(current_date_and_time) #Get current date
        current_time = datetime.datetime.time(current_date_and_time) #Get current time

        if self.cancelled: #The event is already cancelled so just return False
            return False

        if self.date > current_date:
            #The event date is in the future, so it's ok to cancel now
            self.cancelled = True
            return True

        print(self.date, self.start_time)
        print(self.date, current_date)
        print(self.start_time, current_time)
        if self.date == current_date:
            #The event is on today so let's make sure the event hasn't already started before cancelling
            if self.start_time > current_time:
                #Event hasn't started yet so we are safe to cancel now
                self.cancelled = True
                return True

        return False