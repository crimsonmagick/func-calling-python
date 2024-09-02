from decimal import Decimal

from hotels.room_inventory import RoomInventory


class Reservation:

    def __init__(self, reservation_id, room_inventory: RoomInventory, reservation_cost: Decimal):
        self.reservation_id = reservation_id
        self.room_inventory = room_inventory
        self.reservation_cost = reservation_cost

    def __str__(self):
        return (f"Reservation [reservation_id: {self.reservation_id}, "
                f"room_inventory: {self.room_inventory}, "
                f"reservation_cost: {self.reservation_cost}")
