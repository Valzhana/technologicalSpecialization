# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
import argparse


FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(filename='task_01.log', encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='check_date',
                                     description='Checking of the date: exists or not',
                                     epilog='check_date("14.07.1567")')
    parser.add_argument('-s', '--str_date', default='01.01.0001', help='Date to check')
    args = parser.parse_args()
    return check_date(f'{args.str_date}')


def leap_year(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    try:
        day, month, year = map(int, str_date.split('.'))
    except ValueError:
        logger.error(f'The date {str_date} must consists of numeric values separated by a dot')
        return None
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and leap_year(year) and day > 29:
        return False
    if month == 2 and not leap_year(year) and day > 28:
        return False
    logger.info(f'{day=}, {month=}, {year=}, leap_year={leap_year(year)}')
    return True


if __name__ == '__main__':
    logger.info('Such a date exists' if check_date(str_date='10.05.1788') else 'No such date exists')
    parse()
