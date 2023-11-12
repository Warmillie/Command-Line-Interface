
def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

contacts = {}

@error_handler
def add(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

def hello_handler():
    return 'Hello, how I can help you?'

@error_handler
def change(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} updated to {new_phone}"
    else:
        raise KeyError(f"Contact {name} not found")

def show_all():
    if not contacts:
        return f'No contacts found'
    else:
        for name, phone in contacts.items():
            result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
   
@error_handler
def get_phone(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise KeyError(f"Contact {name} not found")




def handle_command(command):
    if command.lower() == "hello":
        return hello_handler()
    elif command.lower().startswith("add"):
        _, name, phone = command.split(" ")
        return add(name, phone)
    elif command.lower().startswith("change"):
        _, name, new_phone = command.split(" ")
        return change(name, new_phone)
    elif command.lower().startswith("phone"):
        _, name = command.split(" ")
        return get_phone(name)
    elif command.lower().startswith("show all"):
         return show_all()
    elif command.lower() == "good bye" or command == "close" or "exit":
        return 'Good bye!'

def main():
    print("Welcome to Contact Assistant!")
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        response = handle_command(user_input)
        print(response)

main()

