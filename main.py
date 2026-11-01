
from venue import Venue
from event import Event
import datetime

#-- 1. Set up a data set:

# Student A - D00290718 - Create 3 Venue objects and store them in an appropriate data structure
venues = [
    Venue(venue_id = 1, name = "Brubakers, Dundalk", capacity = 150),
    Venue(venue_id = 2, name = "Imperial Hotel, Dundalk", capacity = 150),
    Venue(venue_id = 3, name = "PJ Carrolls Building - P1139 Lecture Hall", capacity = 100)
]

# Student A - D00290718 - Create 5 Event objects and store them in an appropriate data structure
# Student A - D00290718 - Done : Each event should be associated with/assigned to one of your venue objects
events = [
    Event(
        event_id = 1,
        title = "DKIT Freshers Day One - Bingo n Beats",
        event_type = "convention",
        date = datetime.date(2026, 9, 21),
        start_time = datetime.time(22, 0),
        capacity = 150,
        venue = venues[0],
        cancelled = False,
        ticket_price = 15.00
    ),

    Event(
        event_id = 2,
        title = "DKIT Freshers Day Two",
        event_type = "convention",
        date = datetime.date(2026, 9, 22),
        start_time = datetime.time(20, 0),
        capacity = 150,
        venue = venues[1],
        cancelled = False,
        ticket_price = 5.00
    ),

    Event(
        event_id = 3,
        title = "Object-Oriented Programming Workshop",
        event_type = "workshop",
        date = datetime.date(2026, 11, 12),
        start_time = datetime.time(11, 0),
        capacity = 80,
        venue = venues[2],
        cancelled = False,
        ticket_price = 0.00
    ),

    Event(
        event_id = 4,
        title = "Software Testing Workshop",
        event_type = "workshop",
        date = datetime.date(2026, 11, 19),
        start_time = datetime.time(10, 0),
        capacity = 60,
        venue = venues[2],
        cancelled = False,
        ticket_price = 0.00
    ),

    Event(
        event_id = 5,
        title = "Solutions Architecture Workshop",
        event_type = "workshop",
        date = datetime.date(2026, 11, 26),
        start_time = datetime.time(12, 0),
        capacity = 100,
        venue = venues[2],
        cancelled = False,
        ticket_price = 0.00
    )
]

# Student B - D00262411 - Create 3 Attendees and store them in an appropriate data structure

"..."

# Student B - D00262411 - Create 5 Bookings and store them in an appropriate data structure
# Student B - D00262411 - Each Booking should be link one of your Attendee objects with one of your Event objects

"..."

#-- 2. Display the information:



# Student A - D00290718 - Display all Venues
print("------------ All Venues: ------------")

for venue in venues:
    print(venue)

# Student B - D00262411 - Display all Bookings, including who is attending and what Event is being held.

"..."

#-- 3. Manipulate the information:

# Student B - D00262411 - Attempt to change the email address on an Attendee to an invalid email, e.g. one without an @ or without a domain included.

"..."


# Student A - D00290718 - Cancel an Event
event_to_cancel = events[4]
cancelled = event_to_cancel.cancel_event()
cancelled_event_title = event_to_cancel.title

print(f"------------ Event '{cancelled_event_title}' cancelled: {cancelled} ------------")

# Student B - D00262411 - Cancel a Booking

"..."

# Student A - D00290718 - Display all active Events (cancelled Events should not be shown)
print("------------ Active Events: ------------")

for event in events:
    if not event.cancelled:
        print(event)

# Student B - D00262411 - Display all cancelled Bookings

"..."

# Student B - D00262411 - Find and display all bookings for a specific Attendee

"..."
