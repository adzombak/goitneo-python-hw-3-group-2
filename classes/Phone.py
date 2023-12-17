from classes import Field


class Phone(Field):
    def __init__(self, phone: str):
        Phone.validate_phone(phone)
        super().__init__(phone)

    @staticmethod
    def validate_phone(phone: str):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError(f"Incorrect phone number format, expected 10 digits but got '{phone}'")
        return True
