#!/usr/bin/python3

# Decorator function to check that we can only pass the correct unit number.
def checkCorrectRoomNumber(func):
    def checkRoomNumber(*arg):
        if (arg[1]) not in ['1A', '1B', '1C', '1D', '1E',
                            '2E', '2D', '2C', '2B', '2A',
                            '3A', '3B', '3C', '3D', '3E',
                            '4E', '4D', '4C', '4B', '4A']:
            return "Invalid Room Number!"
        else:
            return func(*arg)

    return checkRoomNumber


class HotelBoutique:
    def __init__(self, roomNumbers, status):
        """init method accept 2 args:
        1. roomNumbers: list of rooms.
        2. status: default to Available."""
        self.roomNumbers = roomNumbers
        self.status = status
        self.roomStatus = {room: self.status for room in self.roomNumbers}

    @checkCorrectRoomNumber
    def unitStatus(self, unitNumber):
        """Return status of single unit."""
        return self.roomStatus[unitNumber]

    def showAllRoomStatus(self):
        """Method to show all rooms and status."""
        print("\nAll Rooms Status.")
        print("******************")
        for room, status in self.roomStatus.items():
            print("{} is {}.".format(room, status))
        print("******************")

    def showAvailableRooms(self):
        """Method to show all rooms that are available."""
        available_room = "Available rooms: "
        roomAvailable = []
        for room in self.roomStatus.keys():
            if self.roomStatus[room] == 'Available':
                roomAvailable.append(room)
        if len(roomAvailable) > 0:
            print("\n{} {}".format(available_room, ', '.join(roomAvailable)))
        else:
            print("No available room.")

    def getAvailableRoom(self):
        """Method to get and return the nearest available room and be occupied."""
        occupied_room_list = []
        for room in self.roomStatus.keys():
            if self.roomStatus[room] == 'Available':
                self.roomStatus[room] = 'Occupied'
                occupied_room_list.append(room)
                return "Room {} was now occupied.".format(room)
        else:
            for room in self.roomStatus.keys():
                if self.roomStatus[room] != 'Available':
                    return "No available room."

    @checkCorrectRoomNumber
    def checkOutRoom(self, roomNumber):
        """Check-out the room and change the state to Vacant."""
        currentState = self.unitStatus(roomNumber)
        if currentState != "Occupied":
            return "Room {} is not being occupied. It is in {} state. Cannot check-out.".format(roomNumber,
                                                                                                currentState)
        else:
            self.roomStatus[roomNumber] = "Vacant"
            return "Room {} is now vacant after check-out.".format(roomNumber)

    @checkCorrectRoomNumber
    def cleanRoom(self, roomNumber):
        """Send the room for cleaning and release to available."""
        currentState = self.unitStatus(roomNumber)
        if currentState == "Vacant":
            self.roomStatus[roomNumber] = "Available"
            return "Room {} was cleaned, it is now {}.".format(roomNumber, self.roomStatus[roomNumber])
        else:
            return "Room {} cannot be clean, is not vacant.".format(roomNumber)

    @checkCorrectRoomNumber
    def markRepair(self, roomNumber):
        """Send the room for repair. Ex. Guest damaged the TV."""
        currentState = self.unitStatus(roomNumber)
        if currentState == "Vacant":
            self.roomStatus[roomNumber] = "Repair"
            return "Room {} is being sent for repair.".format(roomNumber)
        else:
            return "Room {} is not vacant, cannot sent for repair.".format(roomNumber)

    @checkCorrectRoomNumber
    def repairedRoom(self, roomNumber):
        """Mark the repaired room to vacant."""
        currentState = self.unitStatus(roomNumber)
        if currentState == "Repair":
            self.roomStatus[roomNumber] = "Vacant"
            return "Room {} is now vacant after repair.".format(roomNumber)
        else:
            return "Room {} is not for repair.".format(roomNumber)

    def __str__(self):
        return self.roomStatus


hotel_building_rooms_available = ['1A', '1B', '1C', '1D', '1E',
                                  '2E', '2D', '2C', '2B', '2A',
                                  '3A', '3B', '3C', '3D', '3E',
                                  '4E', '4D', '4C', '4B', '4A']


# if odd number, create 10 rooms, with 1A, 3B, 5C
# if even numbers, create 5 rooms, with 2A, 4B


def createRoomNumber():
    suffix_10_rooms = 'ABCDEFGHIJ'
    suffix_5_rooms = 'ABCDE'
    roomOdd = []
    roomEven = []
    for i in range(1, 20 + 1):
        if i % 2 == 0:
            roomOdd.append(str(i))
        if i % 2 != 0:
            roomEven.append(str(i))
    return roomOdd, roomEven


print(createRoomNumber())


# A user can call the object hotel using dot (.) notation with methods.
hotel = HotelBoutique(hotel_building_rooms_available, "Available")
