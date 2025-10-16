from ex001 import dec_to_bin
from ex002 import bin_to_dec

def to_fixed_width_bin(n: int, bits: int) -> str:
    n = dec_to_bin(n)
    return f'{n:0>{bits}}'

def test_to_fixed_width_bin():
    tests = {
        (5, 8): '00000101',
        (12, 14): '00000000001100',
        (29, 3): '11101'
    }

    for number, bits in tests.keys():
        assert to_fixed_width_bin(number, bits) == tests[(number, bits)], \
        f'Test error, {to_fixed_width_bin(number, bits)} (invalid) is not equal to {tests[(number, bits)]} (correct)'

    print('All tests of to_fixed_width_bin worked!')

def ipv4_to_bin(ip: str) -> str:
    binary_ip = []

    for byte in ip.split('.'):
        binary_ip.append(to_fixed_width_bin(byte, 8))

    return '.'.join(binary_ip)

def test_ipv4_to_bin():
    tests = {
        '192.168.0.1': '11000000.10101000.00000000.00000001',
        '0.0.0.0': '00000000.00000000.00000000.00000000',
        '255.255.255.255': '11111111.11111111.11111111.11111111',
        '255.0.255.0': '11111111.00000000.11111111.00000000',
        '0.255.0.255': '00000000.11111111.00000000.11111111',
        '8.8.8.8': '00001000.00001000.00001000.00001000'
    }

    for number in tests.keys():
        assert ipv4_to_bin(number) == tests[number], \
        f'Test error, {ipv4_to_bin(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of ipv4_to_bin worked!')

def bin_to_ipv4(bits: str) -> str:
    ip = []

    for b in bits.split('.'):
        ip.append(str(bin_to_dec(b)))

    return '.'.join(ip)

def test_bin_to_ipv4():
    tests = {
        '11000000.10101000.00000000.00000001': '192.168.0.1',
        '00000000.00000000.00000000.00000000': '0.0.0.0',
        '11111111.11111111.11111111.11111111': '255.255.255.255',
        '11111111.00000000.11111111.00000000': '255.0.255.0',
        '00000000.11111111.00000000.11111111': '0.255.0.255',
        '00001000.00001000.00001000.00001000': '8.8.8.8'
    }

    for number in tests.keys():
        assert bin_to_ipv4(number) == tests[number], \
        f'Test error, {bin_to_ipv4(number)} (invalid) is not equal to {tests[number]} (correct)'

    print('All tests of bin_to_ipv4 worked!')

if __name__ == '__main__':
    test_to_fixed_width_bin()
    test_ipv4_to_bin()
    test_bin_to_ipv4()