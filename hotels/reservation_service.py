from typing import List, Optional

from hotels.reservation import Reservation
from hotels.room_inventory_repository import RoomInventoryRepository


class ReservationService:

    def __init__(self, room_repository: RoomInventoryRepository):
        self._room_repository = room_repository
        self._reservations: List[Reservation] = []

    def reserve(self, hotel_id: int, sequence_number: int) -> Optional[Reservation]:
        inventory = self._room_repository.get_room_inventory(hotel_id, sequence_number)
        if inventory is not None:
            if inventory.room_count == inventory.rooms_reserved:
                raise Exception(f"No inventory remaining for room_type: {inventory.room_type}")
            reservation_id = len(self._reservations) - 1
            new_reservation = Reservation(reservation_id, inventory, inventory.rate)
            self._reservations.append(new_reservation)
            return new_reservation
        else:
            return None
