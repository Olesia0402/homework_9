import re


phone_book = list()
list_parser_word = ['add', 'change', 'phone', 'show all']


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            print('Enter a write function. Try again.')
        except ValueError:
            print('You enter a wrong value. Try again.')
        except IndexError:
            print('You enter a wrong index. Try again.')

    return inner



def parser_input(sentence):
    return re.findall(r'\w+', sentence)


@input_error
def add_contact(name, phone):
    contact = {name: phone}
    return phone_book.append(contact)


@input_error
def change_contact(name, new_phone):
    phone_book[name] = new_phone
    return print(f'You change phone number for contact {name.title()}.')


@input_error
def show_number_of_phone(name):
    return phone_book[name]


def handler(parser_word):
    if parser_word == 'add':
        return add_contact
    elif parser_word == 'change':
        return change_contact
    elif parser_word == 'phone':
        return show_number_of_phone
    elif parser_word == 'show all':
        return phone_book
    else:
        print('Invalid command. Try again.')


def main():
    print('Hello!')
    while True:
        user_input = input('Enter your command:').lower()
        if user_input == 'hello':
            print("How can I help you?")
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            parser_word, name, phone = parser_input(user_input)
            command = handler(parser_word)
            print(f'Your command {parser_word} was added successfully.')


if __name__ == '__main__':
    main()


