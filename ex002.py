import re

def bin_to_dec(b: str) -> int:
    if not re.match('^-?[01]+$', b):
        raise TypeError('This function only supports binary integers!')
    
    if b[0] == '-':
        negative = True
        b = b[:0:-1]
    else:
        negative = False
        b = b[::-1]

    decimal = int(0)

    for i, number in enumerate(b):
        decimal += int(number) * 2 ** i

    return decimal * -1 if negative else decimal

def test_bin_to_dec():
    tests = {
        '1101': 13,
        '-1000': -8,
        '0': 0
    }

    for number in tests.keys():
        assert bin_to_dec(number) == tests[number], \
        f'Test error, {bin_to_dec(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of bin_to_dec worked!')

if __name__ == '__main__':
    test_bin_to_dec()