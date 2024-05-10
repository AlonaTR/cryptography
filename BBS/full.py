import sympy
import random
from itertools import groupby
from collections import Counter

def bbs(size):
    result = []

    p = sympy.randprime(40000, 50000)
    while p % 4 != 3:
        p = sympy.nextprime(p)

    q = sympy.randprime(40000, 50000)
    while q % 4 != 3 and q != p:
        q = sympy.nextprime(q)

    N = p * q
    s = random.randrange(2, N-1)  #Wybór losowej liczby s której N jest względnie pierwsze
    x0 = pow(s, 2, N)

    count = 0
    while count != size:
        x = (x0 * x0 + 1) % N  # Changed the way x is calculated
        result.append(x0 & 1)
        x0 = x
        count += 1

    return result


def single_bit_test(bits):
    min_value = len(bits) // 2 - len(bits) // 100
    max_value = len(bits) // 2 + len(bits) // 100
    # print(min_value, max_value)
    count_bit = sum(bits)

    if min_value < count_bit < max_value:
        print('Test "Jednego Bitu" Zaliczony. Suma jednek w rzędzie wynosi', count_bit)
        return True
    else:
        print('Test "Jednego Bitu" Niezaliczony. Suma jednek w rzędzie wynosi', count_bit)
        return False

def series_test(bits):
    longest_series = 0
    current_series = 1
    value = bits[0]

    for i in range(1, len(bits)):
        if value == bits[i]:
            current_series += 1
            if current_series > longest_series:
                longest_series = current_series
        else:
            current_series = 1
            value = bits[i]

    print("Test Serii: Najdłuższa seria =", longest_series, "o wartości", value)
    return {'najdluzszaSeria': longest_series, 'wartosc': value}

def long_series_test(bits):
    max_run_length = 26  # Maksymalna długość serii, która zalicza test
    run_lengths = [len(list(run)) for bit, run in groupby(bits)]

    if max(run_lengths) <= max_run_length:
        print("Test Długiej Serii Zaliczony")
        return True
    else:
        print("Test Długiej Serii Niezaliczony")
        return False

from collections import Counter

def poker_test(bits):
    chunk_size =4
    num_segments = len(bits) // chunk_size
    segments = [bits[i:i + chunk_size] for i in range(0, len(bits), chunk_size)]
    
    # Liczenie liczby wystąpień każdej wartości
    occurrences = Counter("".join(map(str, segment)) for segment in segments)
    
    # Liczenie wartości chi-square
    chi_square = (16 / num_segments) * sum(occurrences[i] ** 2 for i in occurrences) - num_segments
    
    print("Wartość chi-square:", chi_square)

    # Przyjęty zakres wartości chi-square dla sukcesu testu
    lower_bound = 2.16
    upper_bound = 46.17

    if lower_bound < chi_square < upper_bound:
        print("Test Chi-square Zaliczony. Wartość chi-square =", chi_square)
        return True
    else:
        print("Test Chi-square Niezaliczony. Wartość chi-square =", chi_square)
        return False



def main():
    num_bits = 20000  # Specify the number of bits to generate

    random_bits = bbs(num_bits)

    # Run FIPS 140-2 tests
    single_bit_test(random_bits)
    series_test(random_bits)
    long_series_test(random_bits)
    poker_test(random_bits)

if __name__ == "__main__":
    main()
