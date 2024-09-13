from decouple import config
from logic import guess_number

number_range = [config("NUMBER_RANGE_START", cast=int), config("NUMBER_RANGE_END", cast=int)]
tries = config("TRIES", cast=int)
start_capital = config("START_CAPITAL", cast=int)

guess_number(number_range, tries, start_capital)