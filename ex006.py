import re

def hex_to_dec(h: str) -> int:
    h = h.upper()

    if not re.match('^-?(\d|[A-F])+$', h):
        raise TypeError('This function only supports hexadecimal integers!')
    
    if h[0] == '-':
        negative = True
        h = h[1:]
    else:
        negative = False

    h = h[::-1]
    
    decimal = int(0)

    numbers = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    for i, number in enumerate(h):
        decimal += int(number) * 16 ** i if number.isdigit() else numbers[number] * 16 ** i

    return -1 * decimal if negative else decimal

def test_hex_to_dec():
    tests = {
        'FF': 255,
        'fff': 4095,
        '-1A': -26
    }

    for number in tests.keys():
        assert hex_to_dec(number) == tests[number], \
        f'Test error, {hex_to_dec(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of hex_to_dec worked!')

if __name__ == '__main__':
    test_hex_to_dec()