from collections import UserDict


class Field:
    """Базовий клас для полів запису ."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту."""
    pass


class Phone(Field):
    """Клас для зберігання номера телефону з перевіркою валідності."""

    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError(
                "Phone number must contain only digits and be 10 digits long."
            )
        super().__init__(value)


class Record:
    """Клас для зберігання інформації про контакт."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Додає новий номер телефону до запису."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """Видаляє телефон із запису, якщо він існує."""
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        """Редагує існуючий номер телефону."""
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return True
        return False

    def find_phone(self, phone):
        """Шукає телефон у списку контактів."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        """Повертає рядкове представлення запису."""
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    """Клас для зберігання та керування записами контактів."""

    def add_record(self, record):
        """Додає запис у книгу контактів."""
        self.data[record.name.value] = record

    def delete(self, name):
        """Видаляє запис за ім'ям, якщо він існує."""
        if name in self.data:
            del self.data[name]
            return True
        return False

    def find(self, name):
        """Повертає запис за ім'ям, якщо він існує."""
        return self.data.get(name, None)
