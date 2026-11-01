import re

def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email) is not None
class attendee:
    def __init__(self, attendee_id, name, email):

        if not isinstance(attendee_id, int) or attendee_id <= 0:
            raise ValueError("Attendee ID must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(email, str) or not validate_email():
            raise ValueError("Invalid email address")

        self.attendee_id = attendee_id
        self.name = name
        self.email = email

    def update_email(self, new_email):
        if isinstance(new_email, str) and validate_email(new_email):
            self.email = new_email
            return True
        return False

    def __str__(self):
        return (
            f"Attendee ID: {self.attendee_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
        )

# Creating an attendee
attendee1 = attendee(101, "Ali Khan", "ali@gmail.com")

# Display attendee information
print(attendee1)

# Update email
result = attendee1.update_email("alikhan@gmail.com")

print("\nEmail updated:", result)

# Display updated information
print(attendee1)