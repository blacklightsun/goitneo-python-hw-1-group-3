from  datetime import datetime, timedelta

def get_birthdays_per_week(users):

    BIRTHDATE_SCOPE = 7
    birthdays_dict = dict()

    today_date = datetime.today().date()
    # today_week_day_number = today_date.week()
    # start_next_week_date = today_date

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today_date.year)
        day_delta = (birthday_this_year - today_date).days
        weekday = birthday_this_year.weekday()

        if day_delta < BIRTHDATE_SCOPE:

            if weekday in [5, 6]:
                birthday_this_year = birthday_this_year + timedelta(days=(7 - weekday))

        if (weekday in birthdays_dict):
            birthdays_dict[weekday].append(name)
        else:
            birthdays_dict[weekday] = [name] 

    print(birthdays_dict)

    days_list = [i for i in birthdays_dict.keys()]

    days_list.sort()

    print(days_list)

    print_text = ''

    for day in days_list:
        for name in day:
            t = ', '.join(birthdays_dict[day]).rstrip(', ') # !!!!!!!!!1

        print_text += f'{birthdays_dict[weekday]}: {t}\n'

    return print_text


def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "1":
            print(get_birthdays_per_week(test_list))

        else:
            print("Invalid command.")


test_list = [
    {"name": "Bill Gates", "birthday": datetime(2024, 3, 3)},
    {"name": "Elon Mask", "birthday": datetime(2024, 10, 15)},
    {"name": "Bill Clinton", "birthday": datetime(2024, 2, 29)},
]

if __name__ == "__main__":
    main()
