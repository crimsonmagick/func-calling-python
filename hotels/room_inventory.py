from hotels.room_type import RoomType


class RoomInventory:
    def __init__(self, hotel_id: int, sequence_number: int, room_type: RoomType, room_count: int):
        self.hotel_id = hotel_id
        self.sequence_number = sequence_number
        self.room_type = room_type
        self.room_count = room_count

    def __str__(self):
        return (f"RoomTypeInventory [hotel_id: {self.hotel_id}, room: {self.room_type}, "
                f"room_count: {self.room_count}]")
