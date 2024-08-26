from typing import List

from .hotel import Hotel


class HotelRepository:

    def __init__(self):
        self.hotels = dict([
            (12, Hotel(12, "Sleep Inn 68th Street", "Phoenix", "AZ", "US", 33, 112))
        ])

    def get(self, hotel_id) -> Hotel:
        return self.hotels[hotel_id]

    def search(self, hotel_name=None, city=None, state=None, country=None, latitude=None, longitude=None) -> List[
                                                                                                            Hotel]:
        results = []
        for hotel in self.hotels.values():
            if city == hotel.city:
                results.append(hotel)
        return results
