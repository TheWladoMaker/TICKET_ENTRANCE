# Version: 0.2 (2021-05-24) still in progress
# This program asks the user for the height of a person in cm and determines 
# if he/she can ride the rollercoaster based on the height.

# Define the class 'Person' with the following attributes:
class Person:
    def __init__(self, name, last_name, age, height, photo):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.photo = photo

    # Method to determine the ticket price based on the age of the person   
    def get_ticket_price(self):
        if 0 < self.age <=12:
            self.ticket_price = 5
        elif 12 < self.age <= 18:
            self.ticket_price = 10
        elif 18 < self.age <= 80:
            self.ticket_price = 15
        else:
            self.ticket_price = None
        return self.ticket_price

    def get_photo(self):
        if self.photo == "\nThey have bought the photography service.":
            self.ticket_price += 3
        elif self.photo == "\nThey have not bought the photography service.":
            self.ticket_price = self.ticket_price
        return self.ticket_price

    # Method to print the information of the person
    def __str__ (self):
        return (f"\nName: {self.name}.\nLast Name: {self.last_name}.\nAge: {self.age},\nHeight: {self.height},\nTicket Price: ${self.ticket_price}\n")

# Function that takes a name and a list of people as parameters and returns the person with that name if it exists in the list, or None otherwise.
def find_person_by_name(name_given, people):
    for person in people:
        if person.name == name_given:
            return person
    return None

# Initialize an empty list to store people
people = []

while True:
    # Ask the user for the height of the person
    while True:
        try:
            height = float(input("\nPlease enter the height in cm: "))
            break
        except ValueError:
            print("\nThat's not a valid option! Please try again.")

    # Check if the person can ride the rollercoaster
    if height >= 120:
        print(f"\nTheir height is {height} cm, they can ride the rollercoaster.")

        # Ask for the person's name and last name
        name = input("\nPlease enter their name: ")
        last_name = input("\nPlease enter their last name: ")

        # Ask for the person's age
        while True:
            try:
                age = int(input("\nPlease enter their age in years: "))
                break
            except ValueError:
                print("\nThat's not a valid option! Please try again.")

        # ask for photography service

        while True:                             
            photo = input("\nWould they like to buy the photography service? Yes or no?: ")
            if photo.lower() == 'yes':
                photo = ("\nThey have bought the photography service.")
                break
            elif photo.lower() == 'no':
                photo = ("\nThey have not bought the photography service.")
                break
            else:
                print("\nThat's not a valid option! Please try again.")

        # Create a new person with the provided information
        person = Person(name, last_name, age, height, photo)

        # Determine and print the person's ticket price 
        ticket_price = person.get_ticket_price()
        photo = person.get_photo()

        if ticket_price is not None:
            print(f"\nThey have to pay ${photo} for the ticket.")
        else:
            print("\nTheir age is not valid, please try again.")
            continue # Go back to the beginning of the loop
    elif 0 < height < 120:
        print(f"\nTheir height is {height} cm, they can't ride the rollercoaster.")
        print("\nThey need to be more than 120 cm tall, if they aren't you have to assign them to another place.\n")
        continue # Go back to the beginning of the loop
    else:
        print(F"\nYour answer is {height} and is not valid, please try again.")
        continue # Go back to the beginning of the loop

    # Add the person to the list of people
    people.append(person)

    # Ask if the user wants to enter another person
    
    while True:
        another = input("\nWould you like to enter another person? Yes or no?: ")
        if another.lower() in ['yes', 'no']: # Check if the input is valid
            break
        else:
            print("\nThat's not a valid option! Please try again.")

    if another.lower() == 'yes':
        continue
    #elif another.lower() == 'no':
    #   break

    while True:
        ask_1 = input("\nWould you like to see the list of people? Or do you want to see the information of a specific person? (list or information): ")
        if ask_1.lower() in ['list', 'information']:
            break
        else:
            print("\nThat's not a valid option! Please try again.")

    # Print the list of people names if the user wants to see it
    if 'information' in ask_1.lower():
        print('\nThese are the names of the people in the list: ')
        for person in people:
            print(person.name)

        while True:
            # Ask for the name of the person the user wants to see the information of
            name_given = input("\nPlease enter the name of the person you want to see the information of: ")
            found_person = find_person_by_name(name_given, people)
            if found_person is not None:
                print(found_person)
                print("\nThanks for using this program!")
                break # if the person is found, print the information and break the loop
            else:
                print("\nThat person is not in the list.")
                # If the person is not found, ask the user if they want to try again
                while True:
                    try_again = input("\nWould you like to try again? Yes or no?: ")
                    if try_again.lower() in ['yes', 'no']:
                        break
                    else:
                        print("\nThat's not a valid option! Please try again.")
                if try_again.lower() == 'yes':
                    continue
                elif try_again.lower() == 'no':
                    break
    # ask if the user wants to enter another person and continue the loop if they do
    while True:
        another_2 = input("\nWould you like to enter another person? Yes or no?: ")
        if another_2.lower() in ['yes', 'no']: # Check if the input is valid
            break
        else:
            print("\nThat's not a valid option! Please try again.")

    if another_2.lower() == 'yes':
        continue
    elif another_2.lower() == 'no':
        print("\nThanks for using this program!")
        break

    elif 'list' in ask_1.lower():
        print("\nThese are the people in the list: ")
        for person in people:
            print(person)
        print("\nThanks for using this program!")