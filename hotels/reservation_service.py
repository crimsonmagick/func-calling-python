from hotels.room_inventory_repository import RoomInventoryRepository


class ReservationService:

    def __init__(self, room_repository: RoomInventoryRepository):
        self.room_repository = room_repository

    def reserve(self, hotel_id, sequence_id):
        return None
