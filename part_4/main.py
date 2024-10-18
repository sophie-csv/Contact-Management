import json

def setup_db():
    """
     Initalizes the contacts.json file and fills it with at least 2 default contacts.
     This is used only once to set up the db structure.
    :return: n/a
    """
    contacts = {
        "current_id": 1,
        "data": {
            "john0": {
                "id": 0,
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "000-000-0000",
                "address": {
                    "street": "123 Main Street",
                    "city": "Atlanta",
                    "state": "Ga",
                    "zipcode": 12345
                },
                "groups": [
                    "CS Pathway",
                    "TSA"
                ]
            },
            "jane1": {
                "id": 1,
                "first_name": "Jane",
                "last_name": "Doe",
                "phone_number": "312-645-0987",
                "address": {
                    "street": "123 Lala Lane",
                    "city": "Orlando",
                    "state": "Fl",
                    "zipcode": 54321
                },
                "groups": [
                    "Eng Pathway",
                    "TSA"
                ]
            }
        }
    }


    f = open("contact_data.json", "w")
    json.dump(contacts, f)
    f.close()


    """
    CNTRL + ALT + L
    """

def write_to_contacts(contacts_dict):
    f = open("contact_data.json", "w")
    json.dump(contacts_dict, f)
    f.close()

def get_contacts_dict():
    """
     Takes no parameters and returns the current contacts.json as a python dict.
     This will be used in other functions to get the current state of the db.
    :return: current contacts.json as a python dict.
    """
    f = open("contact_data.json", "r")
    contacts = json.load(f)
    f.close()
    return contacts

def get_contact_info():
    """
    gets all the info from user input
    """

    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    phone_number = input("Enter the phone number: ")
    street = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    zipcode = input("Enter the zipcode: ")
    groups = []
    num_groups = input("Enter the number of: ")
    for i in range(int(num_groups)):
        group = input("Enter the group: ")
        groups.append(group)

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "address": {
        "street": street,
        "city": city,
        "state": state,
        "zipcode": zipcode
        },
        "groups": groups
    }
    return contact

def add_contact(contact_info):
     contacts = get_contacts_dict()
     contacts["current_id"] += 1
     contact_info["id"] = contacts["current_id"]
     key = contacts["first_name"].lower() + str(id)
     contacts[key] = contact_info
     write_to_contacts(contacts)

def get_contacts_by_id(id):
    contacts = get_contacts_dict()
    for contact in contacts["data"]:
        if contacts["data"][contact]["id"] == id:
            return contact
    return False

def remove_contact(id):
    data = get_contacts_dict()
    contact = get_contacts_by_id(id)
    del data[contact]
    write_to_contacts(data)



def update_contact(id, contact_info):
    data = get_contacts_dict()
    contact = get_contacts_by_id(id)
    data.update(contact, contact_info)
    json.dump(data)


def print_formatted_contact(contact):
    contacts = get_contacts_dict()
    c = contacts["data"][contact]
    print(c["last_name"] + "," + c["first_name"])
    print(c["phone_number"])
    print(c["address"]["street"])
    print(c["address"]["city"] + "," + c["address"]["state"] + " " + str(c["address"]["zipcode"]))
    print(c["groups"])
    print(c["id"])

def print_contacts_from_id_list(id_list):
    count = 0
    contacts = get_contacts_dict()
    for contact in contacts["data"]:
        get_contacts_by_id(contacts["data"][contact]["id"])
        for id in id_list:
            if id == contacts["data"][contact]["id"]:
                print_formatted_contact(get_contacts_by_id(contacts["data"][contact]["id"]))
                count += 1
    if count == 0:
        print("No Contact Found")


def get_contacts_by_first_name(first_name):
    contacts = get_contacts_dict()
    id_list = []
    for contact in contacts["data"]:
        if contacts["data"][contact]["first_name"] == first_name:
            id_list.append(get_contacts_by_id(contacts["data"][contact]["first_name"]))
    print_contacts_from_id_list(id_list)

def get_contacts_by_last_name(last_name):
    contacts = get_contacts_dict()
    id_list = []
    for contact in contacts["data"]:
        if contacts["data"][contact]["last_name"] == last_name:
            id_list.append(get_contacts_by_id(contacts["data"][contact]["last_name"]))
    print_contacts_from_id_list(id_list)


def get_contacts_by_group(group):
    contacts = get_contacts_dict()
    id_list = []
    for contact in contacts["data"]:
        for thegroup in contacts["data"][contact]["groups"]:
            if thegroup == group:
                id_list.append(get_contacts_by_id(contacts["data"][contact]["groups"]))
    print_contacts_from_id_list(id_list)

def get_contacts_by_city(city):
    contacts = get_contacts_dict()
    id_list = []
    for contact in contacts["data"]:
        if contacts["data"][contact]["address"]["city"] == city:
            id_list.append(get_contacts_by_id(contacts["data"][contact]["address"]["city"]))
    print_contacts_from_id_list(id_list)

def get_contacts_by_state(state):
    contacts = get_contacts_dict()
    id_list = []
    for contact in contacts["data"]:
        if contacts["data"][contact]["address"]["state"] == state:
            id_list.append(get_contacts_by_id(contacts["data"][contact]["address"]["state"]))
    print_contacts_from_id_list(id_list)

def search_contact():
    contacts = get_contacts_dict()
    search = input("Enter: 1-first name, 2-last name, 3-group, 4-city, 5-state:   " )
    term = input("Enter search term: ")
    if search == "1":
        get_contacts_by_first_name(term)
    if search == "2":
        get_contacts_by_last_name(term)
    if search == "3":
        get_contacts_by_group(term)
    if search == "4":
        get_contacts_by_city(term)
    if search == "5":
        get_contacts_by_state(term)

def print_all_contacts():
    contacts = get_contacts_dict()
    for contact in contacts["data"]:
        print_formatted_contact(contact)


setup_db()
while True:
    term =  input("Enter: \n 1- Add Contact \n 2- Remove Contact \n 3- Update Contact \n 4- Print one contact \n 5- Print contacts from ID list \n 6- search contacts based on one term \n 7- Print all contacts \n 8- to end \n ENTER HERE: ")
    if term == "8":
        break
    if term == "1":
        add_contact(get_contact_info())
    if term == "2":
        remove_contact(get_contact_info())
    if term == "3":
        id = input("Enter the contact id: ")
        update_contact(id, get_contact_info())
    if term == "4":
        key = input("Enter the contact key: ")
        print_formatted_contact(key)
    if term == "5":
        id_list = []
        many = input("Enter the number of ids: ")
        for i in range(int(many)):
            id = input("Enter the contact id: ")
            id_list.append(id)
        print_contacts_from_id_list(id_list)
    if term == "6":
        search_contact()
    if term == "7":
        print_all_contacts()




