from datetime import datetime

from classes import Field


class Birthday(Field):
    def __init__(self, birthday):
        Birthday.validate_birthday(birthday)
        super().__init__(birthday)

    @staticmethod
    def validate_birthday(birthday):
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
            return True
        except ValueError:
            raise ValueError(f"Incorrect birthday format, expected 'DD.MM.YYYY' but got '{birthday}'")
