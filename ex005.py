def dec_to_hex(n: int) -> str:
    try:
        n = int(n)
    except:
        raise TypeError('This function only supports decimal integers!')

    if n < 0:
        negative = True
        n *= -1
    else:
        negative = False

    restos = []

    letters = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    while (n / 16) != 0:
        restos.append(str(n % 16) if n % 16 < 10 else letters[n % 16])
        n //= 16

    restos.reverse()
    return '-' + ''.join(restos) if negative else ''.join(restos)

def test_dec_to_hex():
    tests = {
        255: 'FF',
        4095: 'FFF',
        -26: '-1A'
    }

    for number in tests.keys():
        assert dec_to_hex(number) == tests[number], \
        f'Test error, {dec_to_hex(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of dec_to_hex worked!')

if __name__ == '__main__':
    test_dec_to_hex()