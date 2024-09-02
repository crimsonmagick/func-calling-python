from typing import List

from hotels import hotel_repository, room_inventory_repository, reservation_service
from hotels.bed_type import BedType
from hotels.room_inventory import RoomInventory

if __name__ == '__main__':

    an_hotel = hotel_repository().get(123)
    print(f"an_hotel: {an_hotel}")
    hotels = hotel_repository().search(city="Phoenix")
    hotel_id = None
    for hotel in hotels:
        print(hotel)
        hotel_id = hotel.hotel_id
        break

    if hotel_id is not None:
        inventory_results: List[RoomInventory] = (
            room_inventory_repository()
            .search_room_inventory(hotel_id,
                                   bed_type=BedType.QUEEN))
        if inventory_results:
            reservation = reservation_service().reserve(hotel_id, inventory_results[0].sequence_number)
            print(reservation)
