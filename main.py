# Anshul Anugu
# Purpose: Upgrading Pet Chooser.
# At every menu, allow the User to quit program.
# Allow user to edit information about the pet.
# Import pet class and sql cursors(use from old code)
import pymysql.cursors
from creds import *
from pets_class import *
pet_list = []
print("Welcome to the Pet Chooser! ")
print("Please select from the options below! ")
def choice_list():
    counter = 1
    for pet in pet_list:
        if counter < 10:
            print(f"[{counter}]  {pet.getPetName()}")
        else:
            print(f"[{counter}] {pet.getPetName()}")
        counter += 1
    # At every menu, give the user the option to [Q] Quit
    print("[Q] Quit")
def pet_edit(pet):
    print(f"You chose to edit {pet.getPetName()}")
    updated_name = input("New name: [ENTER == no change] ")
    try:
        if updated_name:
            pet.setPetName(updated_name)
            print(f"The pet's name is updated to {pet.getPetName()}")
        else:
            print("No update has been made! ")
    except Exception as e:
        print(f"An error occurred: {e}")
        print()
    updated_age = input("New age: [ENTER == no change] ")
    try:
        if updated_age:
            if int(updated_age):
                pet.setPetAge(updated_age)
                print(f"The pet's Age is now {pet.getPetAge()}")
        else:
            print("No update has been made! ")
    except Exception as e:
        print(f"An error occurred: {e}")
# Use Try block from in class example to connect
try:
    connection = pymysql.connect(host=host,
                                 user=username,
                                 password=password,
                                 db=database,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
# Have the exception statement to catch
except Exception as e:
    print("An error has occurred. Please recheck! ")
    print(e)
    exit()
# Create try block and use the sql command line code
try:
    with connection.cursor() as cursor:
        # Insert the long SQL code here
        sql = "Select pets.name as pets_name, pets.age, owners.name as owner, pets.id as id, types.animal_type as animal from pets join owners on pets.owner_id = owners.id join types on pets.animal_type_id = types.id;"
        cursor.execute(sql)
        # Create a for loop here. Create a temporary pet variable to store.
        for row in cursor:
            tempPet = Pet(petId=row['id'],
                animalType=row['animal'],
                owner=row['owner'],
                petAge=row['age'],
                petName=row['pets_name'])
            pet_list.append(tempPet)
except Exception as e:
    print("An error has occurred. Please re-check!")
    print(e)
finally:
    connection.close()
while True:
    choice_list()
    choice = ""
    # Use a try block for capture the if statements within
    try:
        pet = input("Please select from the list: ")
        if pet.upper() == "Q":
            print("Thank you. We hope to see you again! ")
            break
        elif 0 < int(pet) <= len(pet_list):
            # counter comes in handy here from above
            tempPet = pet_list[int(pet) - 1]
            print(f"You chose {tempPet.getPetName()}, the {tempPet.getAnimalType()}.  {tempPet.getPetName()} is {tempPet.getPetAge()} years old.  {tempPet.getPetName()}'s owner is {tempPet.getOwnerName()}.")
            choice = input("Would you like to [C]ontinue, [Q]uit, or [E]dit this pet? ")
            # Allow the user to quit at every menu
            if choice.upper() == "Q":
                print("Thank you. We hope to see you again! ")
                break
            # Allow user to edit their choice if they wish
            elif choice.upper() == "E":
                pet_edit(tempPet)
            # No need to have one for [C] as it will pass.
            else:
                pass
        else:
            print(f"{pet} is not a valid choice Try Again.")
            input("Press [ENTER] to continue.")
    # Use exception to wrap things up
    except Exception as e:
        print(f"{pet} is an invalid choice: {e}")
        input("Press [ENTER] to continue.")
