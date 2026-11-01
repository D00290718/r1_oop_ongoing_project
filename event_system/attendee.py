class attendee:
    def __init__(self, attendee_id, name, email):

        #validating attendee id name and email
        if not isinstance(attendee_id, int) or attendee_id <= 0:
            raise ValueError("Attendee ID must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        if isinstance(email, str):
            valid_email = email.split('@')
            if len(valid_email) != 2:
                raise ValueError("Provided email is invalid")
            user = valid_email[0]
            domain = valid_email[1]

            if user == '' or domain == '':
                raise ValueError("Provided email is invalid")
            if "." not in domain:
                raise ValueError("Provided email is invalid")
            if domain.startswith('.') or domain.endswith('.'):
                raise ValueError("Provided email is invalid")
        else:
            raise ValueError("Email address must be a string")


        self.attendee_id = attendee_id
        self.name = name
        self.email = email

    def update_email(self, new_email):


        if isinstance(new_email, str):
            valid_new_email = new_email.split('@')
            if len(valid_new_email) != 2:
                return False
            new_user = valid_new_email[0]
            new_domain = valid_new_email[1]

            if new_user == '' or new_domain == '':
                return False
            if "." not in new_domain:
                return False
            if new_domain.startswith('.') or new_domain.endswith('.'):
                return False
            self.email = new_email
            return True
        else:
            return False

    def __str__(self):
        return (
            f"Attendee ID: {self.attendee_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
        )


attendeeid = int(input("Enter attendee ID: "))
name = input("Enter attendee name: ")
email = input("Enter attendee email: ")
# Creating an attendee
attendee1 = attendee(attendeeid, name, email)

# Display attendee information
print("\nResult Before Update:")
print(attendee1)

# Update email
result = attendee1.update_email(str(input("Enter new email: ")))
print(result)

print("\nEmail updated:", result)

# Display updated information
print("\nResult After Update:")
print(attendee1)