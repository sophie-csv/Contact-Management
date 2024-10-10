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
    for contact in contacts:
        if contact["data"]["id"] == id:
            return contact
    else:
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
    contact = get_contacts_dict()
    c = contact["data"]
    print(c["last_name"] + "," + c["first_name"])
    print(c["phone_number"])
    print(c["address"]["street"])
    print(c["city"] + "," + c["state"] + c["zipcode"])
    print(c["groups"])
    print(c["id"])

temp = get_contacts_dict()
print(temp)
temp["current_id"] = 100
print(temp)
write_to_contacts(temp)



