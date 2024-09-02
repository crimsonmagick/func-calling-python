from decimal import Decimal
from typing import Optional, List

from .bed_type import BedType
from .room_inventory import RoomInventory
from .room_type import RoomType


class RoomInventoryRepository:
    def __init__(self):
        hotel_id = 12
        self._hotel_inventory = dict([(hotel_id, self.__produce_by_hotel_id(hotel_id))])

    @staticmethod
    def __produce_by_hotel_id(hotel_id):
        return [RoomInventory(hotel_id, 0, RoomType(BedType.QUEEN, 2), 20, Decimal("89.99"))]

    def get_room_inventory(self, hotel_id, sequence_number) -> Optional[RoomInventory]:
        if self._hotel_inventory[hotel_id] is not None:
            for inventory in self._hotel_inventory[hotel_id]:
                if sequence_number == inventory.sequence_number:
                    return inventory
        return None

    def search_room_inventory(self, hotel_id: int, bed_type: BedType = None, room_count: int = None) -> List[
                                                                                                        RoomInventory]:
        matching_rooms = []
        if self._hotel_inventory[hotel_id] is not None:
            for inventory in self._hotel_inventory[hotel_id]:
                if inventory.room_type.bed_type == bed_type or inventory.room_count == room_count:
                    matching_rooms.append(inventory)
        return matching_rooms
