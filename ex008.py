from ex001 import dec_to_bin

def decfrac_to_bin(x: float, max_frac_bits: int = 16) -> str:
    try:
        first, last = str(x).split('.')
    except:
        raise TypeError('This function only supports fractional decimal numbers!')

    first = dec_to_bin(first)
    last = float(f'0.{last}')

    restos = []

    for _ in range(max_frac_bits):
        last *= 2
        last = str(last)
        restos.append(last[0])

        last = last.split('.')[1]
        if last == '0': break
        last = float(f'0.{last}')

    return first + '.' + ''.join(restos)

def test_decfrac_to_bin():
    tests = {
        (10.625, 8): '1010.101',
        (0.1, 10): '0.0001100110',
        (-10.5, 16): '-1010.1'
    }

    for number, max_frac_bits in tests.keys():
        assert decfrac_to_bin(number, max_frac_bits) == tests[(number, max_frac_bits)], \
        f'Test error, {decfrac_to_bin(number, max_frac_bits)} (invalid) is not equal to {tests[(number, max_frac_bits)]} (correct)'

    print('All tests of decfrac_to_bin worked!')

if __name__ == '__main__':
    test_decfrac_to_bin()