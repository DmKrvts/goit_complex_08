from datetime import date, datetime, timedelta

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

def get_birthdays_per_week(users):
    now = date.today()
   
    if not users:
        return {}    
    else:
        birthdays_per_week = {'Monday': [] , 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    for user in users:
        user_birthday = user.get('birthday').replace(year=now.year)
        if user_birthday < now:  # якщо найближчий день народження менше поточної дати...
            user_birthday = user_birthday.replace(year=now.year + 1)
        if now <= user_birthday <= now + timedelta(days=7):
            try:
                user_happy_day = WEEKDAYS[user_birthday.weekday()]
            except IndexError:
                user_happy_day = WEEKDAYS[0]

            birthdays_per_week[user_happy_day].append(user.get('name'))
    res = {key: val for key, val in birthdays_per_week.items() if val} # формуємо фінальний словник, виключаючи дні без свят
    

    return res

if __name__ == "__main__":
    users = [
        {"name": "Wolverine", "birthday": datetime(1956, 11, 4).date()},
        {"name": "Jessica Jones", "birthday": datetime(1996, 11, 5).date()},
        {"name": "Peter Parker", "birthday": datetime(1996, 11, 6).date()},
        {"name": "Stephen Strange", "birthday": datetime(1976, 11, 7).date()},
        {"name": "Wanda Maximov", "birthday": datetime(1986, 11, 8).date()},
        {"name": "Clark Kent", "birthday": datetime(1976, 11, 9).date()},
        {"name": "Diana Prince", "birthday": datetime(1976, 11, 10).date()},
        {"name": "Tony Stark", "birthday": datetime(1976, 11, 11).date()},
        {"name": "Steve Rogers", "birthday": datetime(1976, 11, 12).date()},
        {"name": "Bruce Wayne", "birthday": datetime(1976, 11, 13).date()},
        {"name": "Bruce Banner", "birthday": datetime(1976, 11, 14).date()}        
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")