import csv
from dataclasses import dataclass

@dataclass
class PhoneContact:
    name: str
    phone: int

class Phone:
    def __init__(self):
        self.contacts:list[PhoneContact] = list()

    def load_contacts_from_csv(self, file:str) -> None:
        with open(file, newline='') as csvfile:
            # Hmmmm it is not exactly a dict...?
            # Ahhhh it is a iterator of dicts
            reader = csv.DictReader(csvfile)
            for row in reader:
                phone_contact = PhoneContact(
                    name=row['Name'],
                    phone=int(row['Phone'].replace('-', ''))
                )
                self.contacts.append(phone_contact)

    def search_contacts(self) -> None:
        search_str = input('Search: ')

        matches = list()
        for contact in self.contacts:
            if search_str.upper() in contact.name.upper():
                matches.append(contact)
            elif search_str in str(contact.phone):
                matches.append(contact)

        for match in matches:
            print(match.name, ':', match.phone)

if __name__ == '__main__':
    my_phone = Phone()

    my_phone.load_contacts_from_csv(
        './labs/contacts.csv'
    )

    my_phone.search_contacts()