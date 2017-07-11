address = {'Dan': 'LA', 'Jay': 'Orange County', 'Steve': 'Torrance'}

def contact(stuff):
    print("""
        Contact List - Please choose from the following options:
        1. Find a contact
        2. Add a contact
        3. Remove a contact
        4. Exit

        """)

    stuff = input('> ')

    if stuff == "1":
        x = input('Name: ')
        if x in address:
            print(address[x])

        else:
            print('This contact does not exist')

    if stuff == "2":
        x = input('New Contact Name: ')
        if x in address:
            print('This person is already in the contact list')

        else:
            address[x] = input('City: ')

    if stuff == "3":
        x = input('Name: ')
        if x in address:
            del address[x]

        else:
            print('This contact does not exist')

    if stuff == "4":
        exit()


contact('north')
