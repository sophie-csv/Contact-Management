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
        print(contacts["data"][contact]["id"])
        get_contacts_by_id(contacts["data"][contact]["id"])
        for id in id_list:
            if id == contacts["data"][contact]["id"]:
                print_formatted_contact(get_contacts_by_id(contacts["data"][contact]["id"]))
                count += 1
    if count == 0:
        print("No Contact Found")


def get_contacts_by_first_name(first_name):
    count = 0
    contacts = get_contacts_dict()
    for contact in contacts["data"]:
        if contact["first_name"] == first_name:
            print_formatted_contact(contacts["data"][contact]["first_name"])
            count += 1
    if count == 0:
        print("No Contact Found")

def get_contacts_by_last_name(last_name):
    count = 0
    contacts = get_contacts_dict()
    for contact in contacts["data"]:
        if contact["last_name"] == last_name:
            print_formatted_contact(contacts["data"][contact]["last_name"])
            count += 1
    if count == 0:
        print("No Contact Found")


def get_contacts_by_group(group):
    contacts = get_contacts_dict()
    id_list = []
    for contact in contacts["data"]:
        if contact["groups"] == group:
            id_list.append(contact["id"])
    print_contacts_from_id_list(id_list)

def get_contacts_by_city(city):
    contacts = get_contacts_dict()
    city_list = []
    for contact in contacts["data"]:
        if contact["city"] == city:
            city_list.append(contact["id"])
    print_contacts_from_id_list(city_list)


print_contacts_from_id_list([0, 1])