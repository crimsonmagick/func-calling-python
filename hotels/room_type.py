from hotels.bed_type import BedType


class RoomType:
    def __init__(self, bed_type: BedType, bed_count: int):
        self.bed_type = bed_type
        self.bed_count = bed_count

    def __str__(self):
        return f"RoomType [bed_type: {self.bed_type}, bed_count: {self.bed_count}"
