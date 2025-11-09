from adress_book import AddressBook, Record, Phone


class BotError(Exception):
    """Єдиний клас для помилок бота з готовими повідомленнями."""

    MESSAGES = {
        "invalid_phone": "Phone number must contain only digits and be 10 digits long.",
        "contact_exists": "Contact already exists. Use 'change' to update.",
        "contact_not_found": "Contact not found.",
        "usage_add": "Usage: add [name] [phone]",
        "usage_change": "Usage: change [name] [new phone]",
        "usage_phone": "Usage: phone [name]",
        "no_contacts": "No contacts found.",
        "too_many_args": "Too many arguments provided.",
    }

    def __init__(self, key):
        self.message = self.MESSAGES.get(key, "Unexpected error.")
        super().__init__(self.message)


# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BotError as e:
            return e.message
        except Exception as e:
            return f"Unexpected error: {e}"

    return inner


# Основні функції
@input_error
def add_contact(args, contacts):
    """Додає новий контакт до адресної книги."""
    if len(args) < 2:
        raise BotError("usage_add")
    if len(args) > 2:
        raise BotError("too_many_args")

    name, phone = args[0], args[1]
    name = name.capitalize()  # нормалізація імені

    if contacts.find(name):
        raise BotError("contact_exists")

    record = Record(name)
    try:
        record.add_phone(phone)
    except ValueError:
        raise BotError("invalid_phone")

    contacts.add_record(record)
    return f"Contact '{name}' added with phone {phone}."


@input_error
def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту."""
    if len(args) < 2:
        raise BotError("usage_change")

    name, new_phone = args[0], args[1]
    name = name.capitalize()  # нормалізація імені

    record = contacts.find(name)
    if not record:
        raise BotError("contact_not_found")

    if record.phones:
        record.phones[0].value = new_phone
        return f"Contact '{name}' updated. New phone: {new_phone}"

    record.add_phone(new_phone)
    return f"Phone added for contact '{name}': {new_phone}"


@input_error
def show_phone(args, contacts):
    """Показує номер телефону за ім'ям контакту."""
    if len(args) < 1:
        raise BotError("usage_phone")

    name = args[0].capitalize()  # нормалізація імені
    record = contacts.find(name)

    if not record:
        raise BotError("contact_not_found")
    if not record.phones:
        return f"Contact '{name}' has no phone numbers."

    phones = ", ".join(p.value for p in record.phones)
    return f"{name}: {phones}"


@input_error
def show_all(contacts):
    """Показує всі збережені контакти."""
    if not contacts.data:
        raise BotError("no_contacts")

    result = "Contacts list:\n"
    for record in contacts.data.values():
        phones = ", ".join(p.value for p in record.phones)
        result += f"{record.name.value}: {phones}\n"

    return result.strip()
