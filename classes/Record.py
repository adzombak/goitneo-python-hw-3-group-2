from classes import Name, Phone
from classes.Birthday import Birthday
from utils.handlers import input_error


class Record:
    def __init__(self, name: str, phone: str):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = None

    @input_error
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    @input_error
    def show_birthday(self):
        if self.birthday is not None:
            return print(f"{self.name.value} was born {self.birthday.value}")
        else:
            return print(f"Birthday for {self.name.value} is not added yet")

    def __str__(self):
        birthday = self.birthday.value if self.birthday else 'not added'
        return f"Contact name: {self.name.value}, phone: {self.phone.value}, birthday: {birthday}"
