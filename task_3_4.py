# Приклад реалізації декоратора

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter command arguments."
    return inner

# Приклад функцій-обробників команд

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args, contacts):
    if not contacts:
        return "No contacts found."
    return "\\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def hello(args, contacts):
    return "How can I help you?"

@input_error
def exit_bot(args, contacts):
    return "Good bye!"

# Словник команд

handlers = {
    "add": add_contact,
    "phone": get_phone,
    "all": show_all,
    "hello": hello,
    "exit": exit_bot,
    "close": exit_bot,
    "goodbye": exit_bot
}
