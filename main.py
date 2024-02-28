from  datetime import datetime, timedelta

def get_birthdays_per_week(users):

    BIRTHDATE_SCOPE = 7
    birthdays_list = list()

    today_date = datetime.today().date()
    # today_week_day_number = today_date.week()
    # start_next_week_date = today_date

    for user in users:
        # name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today_date.year)

        if (birthday_this_year - today_date).days < BIRTHDATE_SCOPE:

            if birthday_this_year.week in [5, 6]:
                offset = 7 - birthday_this_year.week
                birthday_this_year = birthday_this_year + timedelta(days=offset)

            birthdays_list.append([user["name"], birthday_this_year.week])

    return birthdays_list


def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "birthdays":
            print(get_birthdays_per_week(test_list))

        else:
            print("Invalid command.")


test_list = [
    {"name": "Bill Gates", "birthday": datetime(2024, 3, 8)},
    {"name": "Elon Mask", "birthday": datetime(2024, 10, 15)}
    ]

if __name__ == "__main__":
    main()
