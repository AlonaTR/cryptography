from random import randint
import numpy as np
import math

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x <= 1:
        return False

    sqrt_x = int(math.sqrt(x))+1

    for n in range(3, sqrt_x, 2):
        if x % n == 0:
            return False
        
    return True


def find_d(e, phi):
    d = 1
    while not ((e * d - 1) % phi == 0):
        d = randint(1, phi)
    return d



if __name__ == '__main__':
    p, q = int(input("p: ")), int(input("q: "))         # 1)podajemy liczbę p i q
    # p=37
    # q=41
    if not (is_prime(p) and is_prime(q)):
        print("p i q muszą być liczbami pierwszymi")
    
    n = p*q                         #2) obliczmy n
    phi = (p-1)*(q-1)               #3) obliczmy phi
    
    e = 2
    while math.gcd(e, phi) != 1:   #4) szukamy liczbę pierwsą dla której najwjększy wspólny dzielnik z phi wynosi 1
        e += 1                     # to i będzie kluczem publicznym
        
    d = find_d(e, phi)              #5) wyliczamy d, to i będzie kluczem prywatnym
    
    print("phi: " + str(phi))
    print("n=(p*q)= " + str(p*q))
    print("public key: " + str(e))
    print("private key: " + str(d))
 