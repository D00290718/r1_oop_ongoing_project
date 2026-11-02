from event_system.venue import Venue
from event_system.event import Event
from event_system.attendee import Attendee
from event_system.booking import Booking
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

attendees = [
    attendee(1001, "Khizar Siddiqui", "khizar@gmail.com"),
    attendee(1002, "Samuel Delaney", "sam@gmail.com"),
    attendee(1003, "Mike Radcliffe", "mike@gmail.com")
]

# Student B - D00262411 - Create 5 Bookings and store them in an appropriate data structure
# Student B - D00262411 - Each Booking should be link one of your Attendee objects with one of your Event objects

bookings = [
    booking(601, attendees[0], event[2]),
    booking(602, attendees[1], event[4]),
    booking(603, attendees[2], event[1]),
    booking(604, attendees[2], event[3]),
    booking(605, attendees[0], event[0])
]

#-- 2. Display the information:



# Student A - D00290718 - Display all Venues
print("------------ All Venues: ------------")

for venue in venues:
    print(venue)

# Student B - D00262411 - Display all Bookings, including who is attending and what Event is being held.

print("------------ All Bookings: ------------")

for booking in bookings:
    print(booking)

#-- 3. Manipulate the information:

# Student B - D00262411 - Attempt to change the email address on an Attendee to an invalid email, e.g. one without an @ or without a domain included.

print("------------ Invalid Email Update: ------------")

attendee_to_update = attendee[0]

print("\nBefore Update")
print(attendee_to_update)

email_result = attendee_to_update.update_email("khizarsiddiqui489.gmail.com")
print("\nEmail updated Successfully")

print("\nAfter Update")
print(attendee_to_update)

# Student A - D00290718 - Cancel an Event
event_to_cancel = events[4]
cancelled = event_to_cancel.cancel_event()
cancelled_event_title = event_to_cancel.title

print(f"------------ Event '{cancelled_event_title}' cancelled: {cancelled} ------------")

# Student B - D00262411 - Cancel a Booking

booking_to_cancel = bookings[4]

print("------------ Before Cancellation: ------------")
print(booking_to_cancel)

booking_to_cancel.cancel()

print("------------ After Cancellation: ------------")
print(booking_to_cancel)

# Student A - D00290718 - Display all active Events (cancelled Events should not be shown)
print("------------ Active Events: ------------")

for event in events:
    if not event.cancelled:
        print(event)

# Student B - D00262411 - Display all cancelled Bookings

print("------------ Cancelled Bookings: ------------")

for booking in bookings:
    if booking.cancelled:
        print(booking)

# Student B - D00262411 - Find and display all bookings for a specific Attendee

print("------------ Bookings for a Specific Attendee: ------------")

attendee_to_find = attendees[3]

print("Attendee:")
print(attendee_to_find)

found_booking = False

for booking in bookings:
    if booking.attendee.attendee_id == attendee_to_find.attendee_id:
        print(booking)
        print("--------------------------")

        found_booking = True

    if not found_booking:
        print("No bookings found for this attendee")

# Additional Demo: Change attendee on a booking

print("------------ Change Booking Attendee: ------------")

booking_to_update_2 = bookings[1]
print("\nBefore Update")
print(booking_to_update_2)

update_result = booking_to_update_2.change_attendee(attendees[2])
print("Attendee updated Successfully")

print("\nAfter Update")
print(booking_to_update_2)
