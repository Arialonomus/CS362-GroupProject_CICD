import re


def convert_integer(int_str, is_hexadecimal):
    """Converts an str of digits representing a decimal or
    hexadecimal integer to an int value"""
    integer_result = 0
    base = 16 if is_hexadecimal else 10
    for char in int_str:
        # Use encoding values to convert characters to digits
        if char.isdigit():
            digit = ord(char) - ord('0')
        else:
            digit = ord(char) - ord('A') + 10
        integer_result = integer_result * base + digit

    return integer_result


def convert_fractional(fractional_str):
    """Converts an str of digits representing an fractional portion
    of a decimal number to a float value"""
    fractional_result = 0
    divisor = 1
    for char in fractional_str:
        digit = ord(char) - ord('0')
        divisor *= 10
        fractional_result += digit / divisor

    return fractional_result


def conv_num(num_str):
    # Validate input is of type str
    if type(num_str) is not str:
        return None

    # Validate input string is not empty
    if len(num_str) < 1:
        return None

    # Strip negative symbol if present
    is_negative = False
    if num_str[0] == '-':
        is_negative = True
        num_str = num_str[1:]

    # Strip hexadecimal prefix, if present
    is_hexadecimal = False
    num_str = num_str.upper()
    if num_str[:2] == '0X':
        is_hexadecimal = True
        num_str = num_str[2:]

    # Validate input string contains valid number of decimal points
    decimal_count = num_str.count('.')
    if decimal_count > 1 or (is_hexadecimal and decimal_count > 0):
        return None

    # Validate input string contains no invalid non-numeric characters
    pattern = r'[^0-9A-F]' if is_hexadecimal else r'[^0-9.]'
    if re.search(pattern, num_str) is not None:
        return None

    # Split string into decimal and integer parts
    if decimal_count == 1:
        integer_part, fractional_part = num_str.split('.')
    else:
        integer_part, fractional_part = num_str, ''

    # Combine the integer and fractional parts or return integer part
    if decimal_count == 0:
        result = convert_integer(integer_part, is_hexadecimal)
    else:
        result = convert_integer(integer_part, False) + convert_fractional(fractional_part)

    # Negate result if string was negative
    if is_negative:
        result = -result

    return result

def leap_year(year: int) -> bool:
    """
    Checks if a year is a leap year or not
    """
    if year % 100 == 0 and year % 400 == 0:
        return True
    else:
        False
        
        
def calculate_year(days: int):
    """
    Takes in the number of days and calculates the year
    """
    year = 1970
    
    while True:
        # Check for leap year
        if leap_year(year):
            days_in_year = 365
        else:
            days_in_year = 366
            
        # Check to see if year has been reached
        if days >= days_in_year:
            days -= days_in_year
            year += 1
        else:
            break

    return days, year

def calculate_month_day(year, days):
    """
    Calculates the month and a day based on year and days
    """
    month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days_reg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 1
    
    if leap_year(year):
        # Use leap year list (29 days in Feb)
        for i in month_days_leap:
            if days >= month_days_leap:
                days -= month_days_leap
                month += 1
            else:
                day = days + 1
                
    else:
        # 28 days in feb
        for i in month_days_reg:
            if days >= month_days_reg:
                days -= month_days_reg
                month += 1
            else:
                day = days + 1
                
    return month, day
    



def my_datetime(num_sec: int) -> str:
    """
    Returns the day-month-year of the number seconds after 01-01-1970
    """
    # Constants
    num_sec_day = 86400
    #year = 1970
    days = num_sec // num_sec_day
    
    year, days_left = calculate_year(days)
    
    pass
