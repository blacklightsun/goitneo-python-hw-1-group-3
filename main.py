from  datetime import datetime, timedelta

def get_birthdays_per_week(users):

    BIRTHDATE_SCOPE = 7 # today and next 6 days
    today_date = datetime.today().date()

    birthdays_dict = dict()
    for user in users:

        name = user["name"]
        birthday_this_year = user["birthday"].date().replace(year=today_date.year)

        weekday = birthday_this_year.weekday()
        if weekday in [5, 6]: # 5, 6 = saturday, sunday
            birthday_this_year = birthday_this_year + timedelta(days=(7 - weekday))

        day_delta = (birthday_this_year - today_date).days # days from today to birthday
        if 0 <= day_delta and day_delta < BIRTHDATE_SCOPE:

            if birthday_this_year not in birthdays_dict:
                birthdays_dict[birthday_this_year] = name + ", " # for first date in dict
            else:
                birthdays_dict[birthday_this_year] += name + ", " # for second and too late dates in dict

    days_list = [i for i in birthdays_dict.keys()]

    days_list.sort()

    print_text = f"\nBirthdays in next {BIRTHDATE_SCOPE} days:\n-------------------------\n"

    for day in days_list:
        print_text += f"{day.strftime('%A'):>10}: {birthdays_dict[day].rstrip(', ')}\n"

    return print_text


def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit", 'quit', 'e']:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command in ["birthdays", 'b']:
            print(get_birthdays_per_week(test_list))

        else:
            print("Invalid command!")


test_list = [
    {"name": "Bill Gates", "birthday": datetime(2024, 2, 26)},
    {"name": "Elon Mask", "birthday": datetime(2024, 3, 5)},
    {"name": "Bill Clinton", "birthday": datetime(2024, 3, 3)},
]

if __name__ == "__main__":
    main()
