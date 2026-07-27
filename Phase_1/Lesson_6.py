#The Phone Directory Search

contacts = {"emihle" : "083 123 4567", "sharon": "082 987 6543", "nashe": "081 234 5678"}

name_to_search = input("Enter the name of the contact you want to search for: ").lower()
for name in contacts:
    if name == name_to_search:
        print(f"Found! {name_to_search}'s number is  {contacts[name_to_search]}")
        break
else:
    print("Contact not found.") 