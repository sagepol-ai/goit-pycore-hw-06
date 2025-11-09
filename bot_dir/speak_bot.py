def handle_speak(command, message=None):
    """
    Обробляє команди та виводить повідомлення користувачу.

    Параметри:
        command (str): команда, яку потрібно обробити.
        message (str, optional): додаткове повідомлення або результат з main_bot.py.
    """
    responses = {
        "welcome": "Welcome to the assistant bot! Send 'hello' to start.",
        "start": (
            "How can I help you? You can add, change, or view contacts. "
            "Type 'help' for assistance."
        ),
        "goodbye": "Good bye!",
        "help": (
            "Available commands:\n"
            "  hello                 – greet the bot\n"
            "  add [name] [phone]    – add a new contact (example: add John 1234567890)\n"
            "  change [name] [phone] – change phone number of an existing contact\n"
            "  phone [name]          – show the phone number of a contact\n"
            "  all                   – show all saved contacts\n"
            "  help                  – show this help message\n"
            "  close / exit          – exit the bot\n\n"
            "Name format: first letter uppercase (e.g., John)\n"
            "Phone format: digits only (e.g., 1234567890)"
        ),
        "add": message,
        "change": message,
        "phone": message,
        "all": message,
        "error": message
    }

    # Отримуємо відповідь з словника або використовуємо передане повідомлення з main_bot.py
    response = responses.get(command, message)

    if response:
        print(response)
