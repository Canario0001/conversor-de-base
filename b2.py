from ex001 import dec_to_bin
from ex002 import bin_to_dec

def sum_one(binary: list[str]) -> list[str]:
    not_found_zero = True
    i = len(binary) - 1
    while not_found_zero and i >= 0:
        if binary[i] == '1':
            binary[i] = '0'
        else:
            binary[i] = '1'
            not_found_zero = False
        i -= 1

    return binary

def flip_bits(binary: list[str]) -> list[str]:
    for i, bit in enumerate(binary):
        if bit == '0':
            binary[i] = '1'
        elif bit == '1':
            binary[i] = '0'
    
    return binary

def to_twos_complement(n: int, bits: int) -> str:
    if n < 0:
        binary = list(f'{dec_to_bin(n)[1:]:0>{bits}}')
    else:
        return f'{dec_to_bin(n):0>{bits}}'

    binary = flip_bits(binary)

    binary = sum_one(binary)

    return ''.join(binary)

def test_to_twos_complement():
    tests = {
        (0, 4): '0000',
        (1, 4): '0001',
        (-1, 4): '1111',
        (-2, 4): '1110',
        (7, 4): '0111',
        (-8, 4): '1000',
    }

    for n, bits in tests.keys():
        assert to_twos_complement(n, bits) == tests[(n, bits)], \
        f'Test error, {to_twos_complement(n, bits)} (invalid) is not equal to {tests[(n, bits)]} (correct)'

    print('All tests of to_twos_complement worked!')

def from_twos_complement(b: str) -> int:
    if b[0] == '0':
        return bin_to_dec(b)
    
    binary = list(b)
    binary = sum_one(flip_bits(binary))

    return -bin_to_dec(''.join(binary))

def test_from_twos_complement():
    tests = {
        '0000': 0,
        '0001': 1,
        '0010': 2,
        '0111': 7,
        '1000': -8,
        '1001': -7,
        '1010': -6,
        '1100': -4,
        '1110': -2,
        '1111': -1,
    }

    for number in tests.keys():
        assert from_twos_complement(number) == tests[number], \
        f'Test error, {from_twos_complement(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of from_twos_complement worked!')

if __name__ == '__main__':
    test_to_twos_complement()
    test_from_twos_complement()