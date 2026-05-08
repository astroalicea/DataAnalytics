contact_info = {
    "Name": "Tony Montana",
    "Address": "47 Maple street",
    "City": "Miami",
    "State": "Florida",
    "Zip": "33135"
}
# Printing address porperlyy formatted for mailing
print(f"{contact_info['Name']}\n {contact_info['Address']}\n {contact_info['City']}, {contact_info['State']}, {contact_info['Zip']}")
del contact_info['Name']
# print(contact_info)
full_name = {
    "first name": "Tony",
    "last name": "Montana"
}
full_name.update({"honorific": "Mr."})
# print(full_name)
contact_info.update({"full name": full_name})
# print(contact_info)

#This will print updated information
print(f"{contact_info['full name']['honorific']} {contact_info['full name']['first name']} {contact_info['full name']['last name']} \n {contact_info['Address']}\n {contact_info['City']}, {contact_info['State']}, {contact_info['Zip']}")
