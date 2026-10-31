#Samuel Delaney - D00290718 - Student A

class Venue:

    def __init__(self, venue_id: int, name: str, capacity: int) -> None:
        """
        Initialises a Venue class object

        Args:
            venue_id (int): Unique ID number for the venue
            name (str): Name of the venue
            capacity (int): Maximum capacity of the venue
        """

        self.__venue_id = venue_id
        self.name = name
        self.capacity = capacity

        #raise ValueError will crash the program and tell the user a custom error message
        # Confirming the capacity is fit for purpose – a capacity cannot be negative
        
        if self.capacity < 0:
            raise ValueError("Capacity cannot be a negative number.")
        if self.capacity == 0: #There needs to be someone there for the purpose of the event
            raise ValueError("Capacity cannot be 0.")

    def __str__(self) -> str:
        """
        Returns all of the information about the venue as a string.
        
        Returns:
            str: The venue ID, name and capacity.
        """

        return f"Venue ID: {self.__venue_id}\nName: {self.name}\nCapacity: {self.capacity}\n"