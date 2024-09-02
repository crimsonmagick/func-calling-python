from typing import List, Optional

from .hotel import Hotel


class HotelRepository:

    def __init__(self):
        self._hotels = dict([
            (12, Hotel(12, "Sleep Inn 68th Street", "Phoenix", "AZ", "US", 33, 112))
        ])

    def get(self, hotel_id) -> Optional[Hotel]:
        if hotel_id in self._hotels:
            return self._hotels[hotel_id]
        return None

    def search(self, hotel_name=None, city=None, state=None, country=None,
               latitude=None, longitude=None) -> List[Hotel]:
        results = []
        for hotel in self._hotels.values():
            if city == hotel.city:
                results.append(hotel)
        return results
