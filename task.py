import re


def conv_num(num_str):
    # Validate input is of type str
    if type(num_str) is not str:
        return None

    # Validate input string is not empty
    str_len = len(num_str)
    if str_len < 1:
        return None

    # Strip negative symbol if present
    is_negative = False
    if num_str[0] == '-':
        is_negative = True
        num_str = num_str[1:]
        str_len -= 1

    # Validate input string contains no invalid non-numeric characters
    if re.search(r'[^0-9.]', num_str) is not None:
        return None

    # Validate input string contains no more than one decimal point
    decimal_count = num_str.count('.')
    if decimal_count > 1:
        return None

    # Split string into decimal and integer parts
    if decimal_count == 1:
        integer_part, fractional_part = num_str.split('.')
    else:
        integer_part, fractional_part = num_str, ''

    # Convert the integer part to an integer
    integer_result = 0
    for char in integer_part:
        # Use encoding values to convert characters to digits
        digit = ord(char) - ord('0')
        integer_result = integer_result * 10 + digit

    # Convert the fractional part to a float
    fractional_result = 0
    divisor = 1
    for char in fractional_part:
        digit = ord(char) - ord('0')
        divisor *= 10
        fractional_result += digit / divisor

    # Combine the integer and fractional parts or return integer part
    if decimal_count == 0:
        result = integer_result
    else:
        result = integer_result + fractional_result

    # Negate result if string was negative
    if is_negative:
        result = -result

    return result
