import re
import string

def convert_base(num: str, base_from: int, base_to: int) -> str:
    num = num.upper()

    if base_from < 2 or base_from > 36 or base_to < 2 or base_to > 36:
        raise TypeError('This function only supports integers from base 2 to base 36!')

    letters = {number:letter for number, letter in enumerate(string.ascii_uppercase, start=10)}
    numbers = dict(zip(letters.values(), letters.keys()))

    valid_chars = string.digits + string.ascii_uppercase
    valid_chars = valid_chars[0:base_from]

    if not re.match(f'^-?[{valid_chars}]+$', num):
        raise ValueError('The number you provided has a different alphabet from the valid alphabet!')

    if num[0] == '-':
        negative = True
        num = num[1:]
    else:
        negative = False
    
    num = num[::-1]
    decimal = int(0)

    for i, number in enumerate(num):
        decimal += int(number) * base_from ** i if number.isdigit() else numbers[number] * base_from ** i

    restos = []

    if decimal == 0: return '0'

    while (decimal / base_to) != 0:
        restos.append(str(decimal % base_to) if decimal % base_to < 10 else letters[decimal % base_to])
        decimal //= base_to

    restos.reverse()
    return '-' + ''.join(restos) if negative else ''.join(restos)

def test_convert_base():
    tests = {
        ('1101', 2, 16): 'D',
        ('-7B', 16, 8): '-173',
        ('zzz', 36, 10): '46655',
        ('0', 10, 2): '0'
    }

    for number, base_from, base_to in tests.keys():
        assert convert_base(number, base_from, base_to) == tests[(number, base_from, base_to)], \
        f'Test error, {convert_base(number, base_from, base_to)} (invalid) is not equal to {tests[(number, base_from, base_to)]} (correct)'

    print('All tests of convert_base worked!')

if __name__ == '__main__' :
    test_convert_base()