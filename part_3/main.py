# phonebook = {}
#
#
# phonebook["John"] = "123-456-7890"
# phonebook["Jane"] = "321-654-0987"
#
# print(phonebook)
# print(phonebook["John"])
# print(phonebook["Jane"])
#
# keys = phonebook.keys()
# values = phonebook.values()
#
# print(keys)
# print(values)
#
# print(list(keys))
# print(list(values))
#
# phonebook = {
#     "John": "123-456-7890",
#     "Jane": "321-654-0987",
#     "Kiki": "333-333-3333",
#     "Shay": "444-444-4444",
#     "Kram": "555-555-5555"
# }
#
# print(phonebook)

###############################################################

# contacts = {
#     "current_id": 1,
#     "John0": {
#         "ID": 0,
#         "first_name": "John",
#         "last_name": "Doe",
#         "phone_number": "123-456-7890",
#         "address": {
#             "Street": "123 Main Street",
#             "City": "Atlanta",
#             "State": "GA",
#             "Zip": 12345
#         },
#         "groups": ["CS Pathway", "TSA"]
#     },
#     "Jane1": {
#         "ID": 1,
#         "first_name": "Jane",
#         "last_name": "Doe",
#         "phone_number": "123-456-7891",
#         "address": {
#             "Street": "123 Lala Street",
#             "City": "Orlanda",
#             "State": "FL",
#             "Zip": 54321
#         },
#         "groups": ["Engineering", "TSA"]
#     }
# }
# print(contacts)
# print(contacts["John0"])
# print(contacts["John0"]["phone_number"])
# print(contacts["John0"]["address"])
# print(contacts["John0"]["address"]["City"])

###############################################################

import json

f = open("contacts.json", "r")
contacts = json.load(f)
print(type(contacts))

contacts["John0"]["phone_number"] = "000-000-0000"
f = open("contacts.json", "w")
json.dump(contacts, f)
f.close()