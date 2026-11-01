from .venue import Venue
import datetime

#Samuel Delaney - D00290718 - Student A

class Event:

    def __init__(
            self,
            event_id: int,
            title: str,
            event_type: str,
            date: datetime.date,
            start_time: datetime.time,
            capacity: int,
            venue: Venue,
            cancelled: bool,
            ticket_price: float

        ) -> None:

        """
        Initialises an Event class object

        Args:
            event_id (int): Unique ID number for the event
            title (str): Title of the event
            event_type (str): Type of event being organised
            date (datetime.date): Date of the event
            start_time (datetime.time): Start time of the event
            capacity (int): Maximum number of people for the event
            venue (Venue): Venue object where the event will be held
            cancelled (bool): If the event has been cancelled or not
            ticket_price (float): Price of a ticket for the event
        """
        self.__event_id = event_id
        self.title = title
        self.event_type = event_type
        self.__capacity = capacity
        self.date = date
        self.start_time = start_time
        self.cancelled = cancelled
        self.ticket_price = ticket_price
        self.venue = venue

        #raise ValueError will crash the program and tell the user a custom error message
        
        # Confirming the capacity is fit for purpose – a capacity cannot be negative

        if self.__capacity < 0:
            raise ValueError("Capacity cannot be a negative number.")
        if self.__capacity == 0: #There needs to be someone there for the purpose of the event
            raise ValueError("Capacity cannot be 0.")

        # Confirming the venue capacity if fit for purpose – the Venue must hold at least the capacity for this Event.

        if not isinstance(venue, Venue): #Without this the next line would crash the program if a venue object was not given
            raise ValueError("Please give a valid Venue object")

        if venue.get_capacity() < self.__capacity:
            raise ValueError("Event Capacity is too big for the Venue's Capacity")

        # Confirming the event type is an allowable value
        self.allowed_event_types = ["workshop", "open day", "conference", "convention"]
        if self.event_type not in self.allowed_event_types:
            raise ValueError("This event type is not allowed. Allowed event types are: workshop, open day, conference, convention")

    def update_schedule(self, new_date: datetime.date, new_start_time: datetime.time) -> None:
        """
        Updates the event date and start time

        Args:
            new_date (datetime.date): The new date for the event
            new_start_time (datetime.time): The new start time for the event
        """
        self.date = new_date
        self.start_time = new_start_time

    def change_venue(self, new_venue: Venue) -> bool:
        """
        Changes the venue only if it has enough capacity

        Args:
            new_venue (Venue): The new venue for the event

        Returns:
            bool: If venue was changed successfully, True will be returned and if not False will be returned
        """
        #First let's make sure that the venue they pass into the function is a real Venue object and if not return False
        if not isinstance(new_venue, Venue):
            return False
        if new_venue.get_capacity() >= self.__capacity: #If the new venue has enough space for the capacity
            self.venue = new_venue #Redefine the old venue to be the new venue
            return True
        return False

    def change_type(self, new_event_type: str) -> bool:
        """
        Changes the event type if the new type is listed in the allowed types.

        Args:
            new_event_type (str): The new event type

        Returns:
            bool: returns True if the event type was changed and if not return False
        """

        if new_event_type in self.allowed_event_types:
            #The new event type is allowed so now redefine the event type to be the new one
            self.event_type = new_event_type
            return True
        #The new event type is not one of the valid options so just return False and don't change anything
        return False
    
    def cancel_event(self) -> bool:
        """
        Cancels the event only if it has not started yet.

        Returns:
            bool: returns True if the event was cancelled and if not will return False
        """

        current_date_and_time = datetime.datetime.now()
        current_date = datetime.datetime.date(current_date_and_time) #Get current date
        current_time = datetime.datetime.time(current_date_and_time) #Get current time

        if self.cancelled: #The event is already cancelled so just return False
            return False

        if self.date > current_date:
            #The event date is in the future, so it's ok to cancel now
            self.cancelled = True
            return True
        
        if self.date == current_date:
            #The event is on today so let's make sure the event hasn't already started before cancelling
            if self.start_time > current_time:
                #Event hasn't started yet so we are safe to cancel now
                self.cancelled = True
                return True

        return False

    def __str__(self) -> str:
        """
        Returns all the event information as a string.

        Returns:
            str: The event ID, title, type, date, time, capacity,
                 venue, cancellation status and ticket price
        """

        return f"Event ID: {self.__event_id}\nTitle: {self.title}\nEvent Type: {self.event_type}\nDate: {self.date}\nStart Time: {self.start_time}\nCapacity: {self.__capacity}\nVenue: {self.venue.name}\nCancelled: {self.cancelled}\nTicket Price: €{self.ticket_price:.2f}\n"