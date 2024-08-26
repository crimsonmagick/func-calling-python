from hotels.hotel_repository import HotelRepository
from hotels.room_inventory_repository import RoomInventoryRepository

room_inventory_repository_singleton = RoomInventoryRepository()
hotel_repository_singleton = HotelRepository()


def room_inventory_repository() -> RoomInventoryRepository:
    return room_inventory_repository_singleton


def hotel_repository() -> HotelRepository:
    return hotel_repository_singleton
