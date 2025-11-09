def read_message(input_message, started):
    """
    Обробляє вхідне повідомлення користувача та визначає команду.

    Параметри:
        input_message (str): текст, введений користувачем.
        started (bool): стан бота (чи активований).

    Повертає:
        tuple: (результат або команда, новий стан started, список аргументів)
    """
    message = input_message.strip().lower()

    # Якщо бот ще не стартував
    if not started:
        if message == "hello":
            return "Start", True, []
        return "Please write 'hello' to start.", False, []

    # Якщо бот вже стартував
    parts = message.split()
    if not parts:
        return "Invalid command.", True, []

    cmd = parts[0]
    args = parts[1:]

    valid_commands = [
        "add", "change", "phone", "all",
        "close", "exit", "hello", "help"
    ]

    if cmd in valid_commands:
        return cmd, True, args

    return "Invalid command.", True, []
