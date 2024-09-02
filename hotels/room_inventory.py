from decimal import Decimal

from hotels.room_type import RoomType


class RoomInventory:
    def __init__(self, hotel_id: int, sequence_number: int, room_type: RoomType, room_count: int, rate: Decimal):
        self.hotel_id = hotel_id
        self.sequence_number = sequence_number
        self.room_type = room_type
        self.room_count = room_count
        self.rooms_reserved = 0
        self.rate = rate

    def __str__(self):
        return (f"RoomInventory [hotel_id: {self.hotel_id}, room: {self.room_type}, "
                f"room_count: {self.room_count}, rooms_reserved: {self.rooms_reserved}, rate: {self.rate}]")
