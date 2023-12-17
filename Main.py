from classes import AddressBook, Record, Name, Phone, Birthday
from utils.handlers import parse_input


def main():
    print("Welcome to the assistant bot!")
    book = AddressBook()
    file_path = 'address_book_data.txt'
    book.load_from_file(file_path)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            book.save_to_file(file_path)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            name, phone = args
            record = Record(name, phone)
            book.add_record(record)
        elif command == "change":
            name, new_phone = args
            print(book.change_phone(name, new_phone))
        elif command == "phone":
            name, = args
            print(book.find_phone(name))
        elif command == "add-birthday":
            name, birthday = args
            record = book.find_record(name)
            if record:
                record.add_birthday(birthday)
                print(f"Birthday added to {name}")
            else:
                print(f"No record found for {name}")
        elif command == "show-birthday":
            name, = args
            record = book.find_record(name)
            record.show_birthday()
        elif command == "birthdays":
            book.get_birthdays_per_week()
        elif command == "all":
            for record in book.get_all_records():
                print(record)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
