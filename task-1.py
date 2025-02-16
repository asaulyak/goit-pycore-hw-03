from datetime import datetime

def get_days_from_today(date):
    date_format = "%Y-%m-%d"
    today = datetime.today()
    parsed_date = datetime.strptime(date, date_format)
    diff = today - parsed_date

    return diff.days
