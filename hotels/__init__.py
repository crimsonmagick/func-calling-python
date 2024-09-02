from hotels.hotel_repository import HotelRepository
from hotels.reservation_service import ReservationService
from hotels.room_inventory_repository import RoomInventoryRepository

hotel_repository_singleton = HotelRepository()
room_inventory_repository_singleton = RoomInventoryRepository()
reservation_service_singleton = ReservationService(room_inventory_repository_singleton)


def room_inventory_repository() -> RoomInventoryRepository:
    return room_inventory_repository_singleton


def hotel_repository() -> HotelRepository:
    return hotel_repository_singleton


def reservation_service() -> ReservationService:
    return reservation_service_singleton
