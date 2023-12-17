import os
import pickle
from collections import UserDict, defaultdict
from datetime import datetime, timedelta

from classes import Record
from utils.handlers import input_error


class AddressBook(UserDict):
    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'rb') as file:
                try:
                    self.data = pickle.load(file)
                except pickle.UnpicklingError:
                    print(f"Cannot load data from {filename}")
        else:
            print(f"No existing data found at {filename}")

    @input_error
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    @input_error
    def find_record(self, name):
        return self.data.get(name, None)

    @input_error
    def find_phone(self, name):
        record = self.find_record(name)
        return f"Phone number is: {record.phone.value}" if record else f"No record found for {name}"

    @input_error
    def change_phone(self, name, new_phone):
        for record in self.data.values():
            if record.name.value == name:
                record.phone.value = new_phone
                return f"The phone number for {name} has been changed to {new_phone}"
        return f"No record found for {name}"

    @input_error
    def get_birthdays_per_week(self):
        birthdays_per_week = defaultdict(list)
        today = datetime.today().date()

        for record in self.data.values():
            name = record.name.value
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value,
                                                      "%d.%m.%Y")  # birthday parse
                birthday_this_year = birthday.replace(year=today.year).date()

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if delta_days < 7:
                    day_of_week = (today + timedelta(days=delta_days)).strftime('%A')
                    if day_of_week in ['Saturday', 'Sunday']:
                        day_of_week = 'Monday'
                    birthdays_per_week[day_of_week].append(name)

        for day, names in birthdays_per_week.items():
            print(f"{day}: {', '.join(names)}")

    def get_all_records(self):
        return iter(self.data.values())
