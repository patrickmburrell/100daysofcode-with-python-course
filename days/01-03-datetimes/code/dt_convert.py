from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    dt = datetime.strptime(date, "%d %b, %Y")
    years = THIS_YEAR - dt.year
    return years


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).%
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    dt = datetime.strptime(date, "%d/%m/%Y")
    american_date = dt.strftime("%m/%d/%Y")
    return american_date


years = years_ago("8 Aug, 2015")
print(f"years: {years}")

us_date = convert_eu_to_us_date("11/03/2002")
print(f"date: {us_date}")
