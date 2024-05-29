import re


def conv_num(num_str):
    # Validate input is of type str
    if type(num_str) is not str:
        return None

    # Validate input string is not empty
    if len(num_str) < 1:
        return None

    # Validate input string contains no more than one decimal point
    if num_str.count('.') > 1:
        return None

    # Validate input string contains no invalid non-numeric characters
    if re.search(r'[^0-9.-]', num_str) is not None:
        return None

    return False
