# This program asks the user for the height of a person in cm and determines 
# if he/she can ride the rollercoaster based on the height.

# Define the class 'Person' with the following attributes:
class Person:
    def __init__(self, name, last_name, age, height):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.height = height

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

        # Create a new person with the provided information
        person = Person(name, last_name, age, height)

        # Determine and print the person's ticket price
        ticket_price = person.get_ticket_price()
        if ticket_price is not None:
            print(f"\nThey have to pay ${ticket_price} for the ticket.")
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
    another = input("\nWould you like to enter another person? Yes or no?: ")
    if another.lower() != 'yes':
        break

while True:
    try:
        ask_1 = input("\nWould you like to see the list of people? Or do you want to see the information of a specific person? (list or information): ")
        break
    except ValueError:
        print("\nThat's not a valid option! Please try again.")

# Print the list of people names if the user wants to see it
if 'information' in ask_1.lower():
    print('These are the names of the people in the list: ')
    for person in people:
        print(person.name)

    # Ask for the name of the person the user wants to see the information of
    name_given = input("\nPlease enter the name of the person you want to see the information of: ")
    found_person = find_person_by_name(name_given, people)
    if found_person is not None:
        print(found_person)
        print("\nThanks for using this program!")
    else:
        print("\nThat person is not in the list.")

elif 'list' in ask_1.lower():
    print("\nThese are the people in the list: ")
    for person in people:
        print(person)
    print("\nThanks for using this program!")