
import random
import math


# check number is prime
def is_prime(number):
    if number < 2:
        return False  # not prime
    for i in range(2, number//2 + 1):  # number//2 +1 half of the numbers
        if number % i == 0:
            return False
    return True

# generate the prime number randomly


def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

# claculate the private key given public key (e) and phi_n


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d*e) % phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")


p, q = generate_prime(1, 100), generate_prime(1, 100)

while p == q:
    q = generate_prime(1, 100)  # to ensure p , q not equal

n = p * q
# claculate phi_n (totient function)
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n-1)  # public key
while math.gcd(e, phi_n) != 1:  # to ensure e coprime with phi_n
    e = random.randint(3, phi_n-1)

d = mod_inverse(e, phi_n)  # private key

message = "Hello RSA "

message_encoded = [ord(ch) for ch in message]  # ASCII for characters

#  encyrept c = m ^ e mod n
cipher_text = [pow(ch, e, n) for ch in message_encoded]

print(cipher_text)
# decrypt m = c ^ d mod n
message_encoded = [pow(ch, d, n) for ch in cipher_text]
plain_text = "".join(chr(ch) for ch in message_encoded)

print(plain_text)
