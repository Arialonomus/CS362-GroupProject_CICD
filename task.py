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
    if num_str.count('.') > 1:
        return None

    # Convert string to integer
    result = 0
    for char in num_str:
        # Use encoding values to convert characters to digits
        digit = ord(char) - ord('0')
        result = result * 10 + digit

    return result
