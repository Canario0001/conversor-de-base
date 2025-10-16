def dec_to_bin(n: int) -> str:
    try:
        n = int(n)
    except:
        raise TypeError('This function only supports decimal integers!')
        
    if n == 0: return '0'
    
    if n < 0:
        negative = True
        n *= -1
    else:
        negative = False
    
    restos = []

    while (n / 2) != 0:
        restos.append(str(n % 2))
        n //= 2

    if negative: restos.append('-')
    restos.reverse()
        
    return ''.join(restos)

def test_dec_to_bin():
    tests = {
        13: '1101',
        0: '0',
        -8: '-1000'
    }
    
    for number in tests.keys():
        assert dec_to_bin(number) == tests[number], \
        f'Test error, {dec_to_bin(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of dec_to_bin worked!')

if __name__ == '__main__':
    test_dec_to_bin()