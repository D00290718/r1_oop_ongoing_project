from datetime import date
from .attendee import attendee
from .event import Event
from .venue import Venue
import datetime

class Booking:

    def __init__(self, booking_id, attendee_val, event_Val, booking_date=None):

        # Validate booking ID
        if type(booking_id) is not int or booking_id <= 0:
            raise ValueError("Booking ID must be a positive integer")

        # Validate attendee
        if not isinstance(attendee_val, attendee):
            raise ValueError("A valid attendee object is required")

        # Validate event
        if not isinstance(event_Val, Event):
            raise ValueError("A valid Event object is required")

        # Set default booking date
        if booking_date is None:
            booking_date = date.today()

        # Validate booking date
        if type(booking_date) is not date:
            raise ValueError("Booking date must be a valid date")

        if booking_date > date.today():
            raise ValueError("Booking date cannot be in the future")

        # Store attributes
        self._booking_id = booking_id
        self._attendee = attendee_val
        self._event = event_Val
        self._booking_date = booking_date
        self._cancelled = False

    # Read-only properties
    @property
    def booking_id(self):
        return self._booking_id

    @property
    def event(self):
        return self._event

    @property
    def booking_date(self):
        return self._booking_date

    @property
    def attendee(self):
        return self._attendee

    @property
    def cancelled(self):
        return self._cancelled

    # Change attendee
    def change_attendee(self, new_attendee):

        if isinstance(new_attendee, attendee):
            self._attendee = new_attendee
            return True

        return False

    # Cancel booking
    def cancel(self):
        self._cancelled = True

    # Display booking information
    def __str__(self):

        return (
            f"Booking ID: {self._booking_id}\n"
            f"attendee: {self._attendee}\n"
            f"Event: {self._event}\n"
            f"Booking Date: {self._booking_date}\n"
            f"Cancelled: {self._cancelled}"
        )



# Create attendees
attendee1 = attendee(101, "Ali Khan", "ali@gmail.com")
attendee2 = attendee(102, "Ahmed", "ahmed@gmail.com")

# Assume you have already implemented Event
test_venue = Venue(venue_id = 1, name = "Brubakers, Dundalk", capacity = 150)
event1 = Event(
    event_id = 1,
    title = "DKIT Freshers Day One - Bingo n Beats",
    event_type = "convention",
    date = datetime.date(2026, 9, 21),
    start_time = datetime.time(22, 0),
    capacity = 150,
    venue = test_venue,
    cancelled = False,
    ticket_price = 15.00
)

# Create booking
booking1 = Booking(501, attendee1, event1)

# Display booking
print(booking1)

# Change attendee
print(booking1.change_attendee(attendee2))

# Cancel booking
booking1.cancel()

# Display updated booking
print(booking1)
