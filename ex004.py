import re

def oct_to_dec(o: str) -> int:
    if not re.match('^-?[0-7]+$', o):
        raise TypeError('This function only supports octal integers!')
    
    if o[0] == '-':
        negative = True
        o = o[:0:-1]
    else:
        negative = False
        o = o[::-1]

    decimal = int(0)

    for i, number in enumerate(o):
        decimal += int(number) * 8 ** i

    return decimal * -1 if negative else decimal

def test_oct_to_dec():
    tests = {
        '135': 93,
        '-100': -64
    }

    for number in tests.keys():
        assert oct_to_dec(number) == tests[number], \
        f'Test error, {oct_to_dec(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of oct_to_dec worked!')

if __name__ == '__main__':
    test_oct_to_dec()
    print(oct_to_dec('127'))