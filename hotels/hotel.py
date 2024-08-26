import string


class Hotel:
    def __init__(self, hotel_id: int, hotel_name: string, city: string, state: string, country: string,
                 lattitude: float, longtitude: float):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.country = country
        self.state = state
        self.city = city
        self.lattitude = lattitude
        self.longtitude = longtitude

    def __str__(self):
        return (f"Hotel [ID: {self.hotel_id}, Name: {self.hotel_name}, City: {self.city}, "
                f"State: {self.state}, Country: {self.country}, "
                f"Latitude: {self.lattitude}, Longitude: {self.longtitude}]")
