"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
from datetime import datetime, date, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = date.today()
    today_day = date.today().day
    today_month = date.today().month
    today_year = date.today().year
    delta_day = timedelta(days=1)
    # более простой способ:
    # prev_month_date = today - timedelta(days=31)
    prev_month_str = str(today_day) + '/' + str(today_month-1) + '/' + str(today_year)
    prev_month_date = datetime.strptime(prev_month_str, '%d/%m/%Y')
    prev_month = prev_month_date.strftime('%Y-%m-%d')

    print("Вчера {}".format(today-delta_day))
    print("Сегодня {}".format(today))
    print("Месяц назад {}".format(prev_month))
    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    str_datetime = datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')
    return str_datetime
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
