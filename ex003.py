def dec_to_oct(n: int) -> str:
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

    while (n / 8) != 0:
        restos.append(str(n % 8))
        n //= 8

    restos.reverse()
    return '-' + ''.join(restos) if negative else ''.join(restos)

def test_dec_to_oct():
    tests = {
        93: '135',
        -64: '-100'
    }

    for number in tests.keys():
        assert dec_to_oct(number) == tests[number], \
        f'Test error, {dec_to_oct(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of dec_to_oct worked!')

if __name__ == '__main__':
    test_dec_to_oct()