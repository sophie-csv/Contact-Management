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



def get_contacts_dict():
    """
     Takes no parameters and returns the current contacts.json as a python dict.
     This will be used in other functions to get the current state of the db.
    :return: current contacts.json as a python dict.
    """

def get_contact_info():
    """

    :return:
    """
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    phone_number = input("Enter the phone number: ")
    street = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    zipcode = input("Enter the zipcode: ")
    groups = input("Enter the groups: ")



get_contact_info()
