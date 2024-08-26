from hotels import hotel_repository, room_inventory_repository
from hotels.bed_type import BedType

if __name__ == '__main__':
    # hotel = hotel_repository.get(123)
    hotels = hotel_repository().search(city="Phoenix")
    hotel_id = None
    for hotel in hotels:
        print(hotel)
        hotel_id = hotel.hotel_id
        break

    if hotel_id is not None:
        # inventory = room_inventory_repository().get_room_inventory(hotel_id, 0)
        for inventory in room_inventory_repository().search_room_inventory(hotel_id, bed_type=BedType.QUEEN):
            print(inventory)
