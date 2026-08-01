from datetime import datetime

from dateutil.relativedelta import relativedelta
from pytz import timezone


def get_hour(city):
    return datetime.now(timezone(city)).strftime('%H:%M')

today = datetime.now(timezone('America/Recife'))
today_is = today.strftime('%d/%m/%Y %H:%M:%S')

name = input('Tip your name: ')

birth_input = input('Tip your date of birth (DD/MM/YYYY): ')

birth_date = (datetime.strptime(birth_input, '%d/%m/%Y').replace(tzinfo=timezone('America/Recife')))
birth_str_fmt = '%d/%m/%Y'
birth_date_str = datetime.strftime(birth_date, birth_str_fmt)

next_birth = birth_date.replace(year=today.year)
# print(next_birth)
delta = relativedelta(today, birth_date)

if next_birth < today:
    # next_birth.timedelta(year=)
    next_birth = next_birth.replace(year=today.year + 1)
    next_birth -= today
else:
    next_birth -= today

time_recife =  get_hour('America/Recife')
time_tokyo = get_hour('Asia/Tokyo')
time_london = get_hour('Europe/London')

print(f'Olá, {name}!')

print(f"""Today is: 
{today_is}

You were born in:
{birth_date_str}

You have been living for:
{delta.years} years
{delta.months} months
{delta.days} days

There are:
{next_birth.days} days left until your next birthday.

Current timestamp:
{today.timestamp():.0f}

Time in Recife:
{time_recife}

Time in Tokyo:
{time_tokyo}

Time in London:
{time_london}
""")