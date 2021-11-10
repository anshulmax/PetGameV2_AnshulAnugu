# Anshul Anugu
# Purpose:  Create pets class so we can use in main.py
# Copy over from petchooserV1.
# Create Private Properties
class Pet:
    __petId = 1
    __animalType = "cat"
    __owner = "Anshul Anugu"
    __petAge = 0
    __petName = "Brady"
    def __init__(self,
                 petId=1,
                 animalType="cat",
                 owner="Anshul Anugu",
                 petAge=0,
                 petName="Brady"):
        self.setPetId(petId)
        self.setAnimalType(animalType)
        self.setOwnerName(owner)
        self.setPetAge(petAge)
        self.setPetName(petName)
    # Create a series of getters and setters
    def getAnimalType(self):
        return self.__animalType
    def setAnimalType(self, animalType):
        # Use Try block here
        try:
            if animalType:
                self.__animalType = animalType
        # Important Exception here to catch empty set
        except Exception as e:
            raise TypeError(f"AnimalType seems to be empty!")
    def getOwnerName(self):
        return self.__owner
    def setOwnerName(self, owner):
        # Use Try block here
        try:
            if owner:
                self.__owner = owner
        except Exception as e:
            # Important Exception here to catch empty set
            raise TypeError(f"Owner seems to be empty!")
    def getPetAge(self):
        return self.__petAge
    def setPetAge(self, petAge):
        # Use Try block here
        try:
            # Accept only integers
            if int(petAge):
                self.__petAge = petAge
        except Exception as e:
            raise TypeError(f"{petAge} does not look like an integer!")
    def getPetId(self):
        return self.__petId
    def setPetId(self, petId):
        # Use Try block here
        try:
            # Accept only integers
            if int(petId):
                self.__petId = petId
        # Use except statement and use the TypeError exception here
        except Exception as e:
            raise TypeError(f"{petId} does not look like an integer!")
    def getPetName(self):
        return self.__petName
    def setPetName(self, petName):
        # Use Try block here
        try:
            if petName:
                self.__petName = petName
        # Use the TypeError exception here
        except Exception as e:
            raise TypeError(f"PetName seems to be empty!")