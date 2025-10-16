import re
import string

def convert_base(num: str, base_from: int, base_to: int, max_frac_bits: int = 16) -> str:
    num = num.upper()

    if base_from < 2 or base_from > 36 or base_to < 2 or base_to > 36:
        raise TypeError('This function only supports integers from base 2 to base 36!')

    letters = {number:letter for number, letter in enumerate(string.ascii_uppercase, start=10)}
    numbers = dict(zip(letters.values(), letters.keys()))

    valid_chars = string.digits + string.ascii_uppercase
    valid_chars = valid_chars[0:base_from]
    
    if not re.match(f'^-?[{valid_chars}]*\\.?[{valid_chars}]*$', num):
        raise ValueError('The number you provided has a different alphabet from the valid alphabet!')

    if num[0] == '-':
        negative = True
        num = num[1:]
    else:
        negative = False
    
    if '.' in num:
        integer_part, fractional_part = num.split('.')
    else:
        integer_part, fractional_part = num, ''
    
    integer_part = integer_part[::-1]
    decimal_integer = 0

    for i, number in enumerate(integer_part):
        decimal_integer += int(number) * base_from ** i if number.isdigit() else numbers[number] * base_from ** i

    decimal_fractional = 0.0
    if fractional_part:
        for i, number in enumerate(fractional_part, start=1):
            decimal_fractional += (int(number) if number.isdigit() else numbers[number]) * (base_from ** -i)

    decimal_total = decimal_integer + decimal_fractional

    restos = []
    integer_value = int(decimal_integer)

    if integer_value == 0:
        integer_result = '0'
    else:
        while integer_value > 0:
            remainder = integer_value % base_to
            restos.append(str(remainder) if remainder < 10 else letters[remainder])
            integer_value //= base_to
        restos.reverse()
        integer_result = ''.join(restos)

    fractional_result = ''
    if fractional_part:
        fractional_value = decimal_total - int(decimal_total)
        fractional_result = '.'
        
        for _ in range(max_frac_bits):
            if fractional_value == 0:
                break
            fractional_value *= base_to
            digit = int(fractional_value)
            fractional_result += str(digit) if digit < 10 else letters[digit]
            fractional_value -= digit

    result = integer_result + fractional_result
    if result == '':
        result = '0'
    
    return '-' + result if negative else result

def test_convert_base():
    tests = {
        ("1010", 2, 10, 8): "10",
        ("10.5", 10, 2, 8): "1010.1",
        ("255.125", 10, 16, 8): "FF.2",
        ("F.C", 16, 10, 8): "15.75",
        ("101.101", 2, 10, 8): "5.625",
        ("5.625", 10, 2, 8): "101.101",
        ("A.8", 16, 10, 8): "10.5",
        ("0.1", 10, 2, 8): "0.00011001"
    }

    for number, base_from, base_to, max_frac_bits in tests.keys():
        assert convert_base(number, base_from, base_to, max_frac_bits) == tests[(number, base_from, base_to, max_frac_bits)], \
        f'Test error, {convert_base(number, base_from, base_to, max_frac_bits)} (invalid) is not equal to {tests[(number, base_from, base_to, max_frac_bits)]} (correct)'

    print('All tests of convert_base worked!')

def main():
    test_convert_base()

if __name__ == '__main__':
    main()
