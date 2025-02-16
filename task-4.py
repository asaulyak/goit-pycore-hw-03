from datetime import datetime, timedelta

def get_upcoming_birthdays(company_users):
    today = datetime.today().date()

    upcoming_birthdays_this_week = []

    for user in company_users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        birthday_this_year = datetime(year=today.year, month=birthday.month, day=birthday.day).date()

        diff_days = (birthday_this_year - today).days
        if 0 <= diff_days < 7:
            congratulation_date = birthday_this_year
            congratulation_date_week_day = congratulation_date.isoweekday()

            if congratulation_date_week_day in [6, 7]:
                congratulation_date_shift = 8 - congratulation_date_week_day
                congratulation_date += timedelta(days = congratulation_date_shift)

            upcoming_birthdays_this_week.append({'name': user["name"], 'congratulation_date': congratulation_date})

    return upcoming_birthdays_this_week



