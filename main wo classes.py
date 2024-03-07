from  datetime import datetime, timedelta
import re



def get_birthdays_per_week(contacts):
    '''
    This function recieves a contact list and returns a list of contacts with birthdays
    today and next 6 days.
    If birthday will be on weekends (Saturday, Sunday) then birthday message would move
    on next Monday.
    '''

    if len(contacts) == 0:
        return '\nNobody is in your contact list. (((\n'

    BIRTHDATE_SCOPE = 7 # today and next 6 days
    WEEKENDS = (5, 6) # 5, 6 = saturday, sunday
    today_date = datetime.today().date()

    birthdays_dict = dict()
    for contact in contacts:

        
        if contact["birthday"] is not None: # checking for empty birthday
            birthday_this_year = contact["birthday"].date().replace(year=today_date.year)
        else:
            break

        weekday = birthday_this_year.weekday()
        if weekday in WEEKENDS: 
            birthday_this_year = birthday_this_year + timedelta(days=(7 - weekday)) # move to Monday

        day_delta = (birthday_this_year - today_date).days # days from today to birthday
        if 0 <= day_delta and day_delta < BIRTHDATE_SCOPE:

            name = contact["name"]
            if birthday_this_year not in birthdays_dict:
                birthdays_dict[birthday_this_year] = name + ", " # for first date in dict
            else:
                birthdays_dict[birthday_this_year] += name + ", " # for second and next dates in dict

    days_list = [i for i in birthdays_dict.keys()]

    if len(days_list) == 0:
        return f"\nNo one celebrates their birthday in next {BIRTHDATE_SCOPE} days. (((\nThrow a party for yourself!!!\n"

    days_list.sort()

    print_text = f"\nBirthdays in next {BIRTHDATE_SCOPE} days:\n-------------------------\n"

    for day in days_list:
        print_text += f"{str(day.strftime('%A'))+":":<12} {birthdays_dict[day].rstrip(', ')}\n"

    return print_text





def get_help():
    '''
    This function returns a user help data.
    '''

    help_string = 'Help will be in next version. )))'
    return help_string





def split_args_with_name(args: tuple):
    '''
    This function recieves a tuple with bot arguments of bot command (without same command) and
    returns tuple of a contact name and tuple ( ( birthdate or/and phone number(s) ) or nothing ).
    Birthdate must be in yyyy-mm-dd format.
    '''

    if len(args) < 1: # case without contact name in command
        return None, None, []
    
    else: # case with contact name in command
        name = args[0]
        birthday = None
        phones = []

        other_args = args[1:]
        for arg in other_args:                                   # search in other args for:
            if re.search("\d{4}-\d{2}-\d{2}", arg) is not None:                              # birthday
                birthday = datetime(
                    int(arg[0:4]),
                    int(arg[5:7]),
                    int(arg[8:]),
                    0, 0, 0,
                    )
            else:                                                                             # or phones
                phones.append(arg) # додаати нормалізацію номерів в наступній версії

    return name, birthday, phones





def get_phones_string(phones: list):
    '''
    This function recieves a phone list of some contact and
    returns a string with all phone numbers or 'No data' string
    '''

    phones_string = ""

    if len(phones) > 0:
        for phone in phones:
            phones_string += phone + ', '
    else:
        phones_string = 'No data'

    return phones_string.rstrip(', ')





def get_birhday_string(birthday: datetime):
    '''
    This function recieves a datetime object, checks for None and
    returns a string with date of birth or 'No data' string.
    '''

    birthday_string = str(birthday.date()) if birthday is not None else 'No data'

    return birthday_string





def add_contact(args: tuple, contacts: list):
    '''
    This function recieves a contact list, a contact name and ( ( birthday or/and phone number(s) )
    or nothing ), adds data in a contact list and returns a string with executing status.
    Birthdate is in yyyy-mm-dd format.
    '''

    name = split_args_with_name(args)[0].capitalize()
    if name is None:
        return 'Sorry, command is without a contacts name.'
    
    for contact in contacts:
        if contact['name'] == name:
            return f'Sorry, but {name} is in your contact list already. (('
        
    birthday = split_args_with_name(args)[1]
    phones = split_args_with_name(args)[2]

    contacts.append(dict([
        ('name', name),
        ('birthday', birthday),
        ('phones', phones)
        ]))
    
    return "Contact added."





def show_all(contacts: list):
    '''
    This function recieves a contact list and returns a string with all contact information.
    '''

    result_string = f"\nYour contact(s):\n-------------------------\n"
    for contact in contacts:
        result_string += f'{contact['name']:<15} -> birtday: {get_birhday_string(contact['birthday'])}, phone(s): {get_phones_string(contact['phones'])}\n'
   
    return result_string





def change_contact(args: tuple, contacts: list):
    '''
    This function recieves a contact list, a contact name and ( ( birthday or/and phone number(s) ) or nothing ),
    changes data in a contact list and returns a string with executing status.
    Birthdate is in yyyy-mm-dd format.
    '''

    name = split_args_with_name(args)[0].capitalize()
    if name is None:
        return 'Sorry, the command is without a contact name.'
    
    new_birthday = split_args_with_name(args)[1]
    new_phones = split_args_with_name(args)[2]
    
    for contact in contacts:
        if contact['name'] == name:

            contact['birthday'] = new_birthday if new_birthday is not None else contact['birthday']
            contact['phones'] = new_phones if len(new_phones) != 0 else contact['phones']
            
            return "Contact updated."

    return f'Sorry, but {name} is not in your contact list yet. (('





def show_phone(args: tuple, contacts: list):
    '''
    This function recieves a contact list and a contact name and
    returns a string with phones of a contact.
    '''

    name = split_args_with_name(args)[0].capitalize() # подумати, як завернути це в декоратор
    if name is None:
        return 'Sorry, command is without a contact name.'
    
    for contact in contacts:
        if contact['name'] == name:

            if len(contact['phones']) > 0:              
                return f'{name}\'s phone(s): {get_phones_string(contact['phones'])}.'
            else:
                return f'No phone(s) saved for {name}.'

    return f'{name} is not in your contact list.'





def main():
    '''
    This is the function with a main wokr cycle for inputing of commands.
    '''

    print("Welcome to the assistant bot!\n")
    while True:

        # парсінг команд виконується стільки ж разів, скільки й головний цикл у main(),
        # тому не бачу сенсу виділяти три рядки коду в окрему функцію і збільшувати кількість рядків з кодом
        command, *args = input("Enter a command: ").strip().split()
        command = command.strip().lower()
        arguments = (*args,)

        # всі функції, які викликаються командами, нічого не друкують, тільки повертають або статус виконання, або відповідь. Друк - в умовному операторі. На наступній ітеріції заверну друк в декоратор.
        if command in ("close", "exit", 'quit', 'e', 'q'):
            print("Good bye!")
            break

        elif command == "hello":
            print("Hello! How can I help you?")

        elif command == "all":
            print(show_all(contact_list))

        elif command in ("help", 'h'):
            print(get_help())        

        elif command in ("birthdays", 'bd'):
            print(get_birthdays_per_week(contact_list))

        elif command in ('add',):
            print(add_contact(arguments, contact_list))

        elif command in ('change',):
            print(change_contact(arguments, contact_list))

        elif command in ('phone',):
            print(show_phone(arguments, contact_list))

        else:
            print("Invalid command!")

# imitation of opening contact list from a file
contact_list = [
    {"name": "Bill_Gates", "birthday": datetime(2024, 3, 26), 'phones': ['0503334589']},
    {"name": "Elon_Mask", "birthday": datetime(2024, 3, 5), 'phones': ['0967894523', '0503216587']},
    {"name": "Bill_Clinton", "birthday": datetime(2024, 3, 3), 'phones': ['0631234556']},
]

if __name__ == "__main__":
    main()
