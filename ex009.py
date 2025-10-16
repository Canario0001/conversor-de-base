from ex002 import bin_to_dec

def binfrac_to_dec(b: str) -> float:
    if b[0] == '-' and b[1] == '0':
        negative = True
    else:
        negative = False
    
    try: 
        decimal, last = b.split('.')
    except:
        raise TypeError('This function only supports fractional binary numbers!')
    
    decimal = bin_to_dec(decimal)

    for i, bit in enumerate(last, start=1):
        decimal += float(bit) * 2 ** -i
    
    return -1 * decimal if negative else decimal

def test_binfrac_to_dec():
    tests = {
        '1010.101': 10.625,
        '-0.01': -0.25
    }

    for number in tests.keys():
        assert binfrac_to_dec(number) == tests[number], \
        f'Test error, {binfrac_to_dec(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of binfrac_to_dec worked!')

if __name__ == '__main__':
    test_binfrac_to_dec()