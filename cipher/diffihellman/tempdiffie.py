import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    while True:
        prime_candidate = random.randint(2**10, 2**15)
        if is_prime(prime_candidate):
            return prime_candidate
            
def is_primitive_root(g, p):
    # Check if g is a primitive root modulo p
    values = set()
    for i in range(1, p):
        values.add(pow(g, i, p))
    return len(values) == p - 1

def generate_primitive_root(p):
    # Find a primitive root modulo p
    while True:
        g = random.randint(2, p - 2)
        if is_primitive_root(g, p):
            return g

def mod_exp(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent //= 2
        base = (base * base) % mod
    return result

def diffie_hellman_key_exchange():
    # Step 1: Select large prime numbers
    p = generate_prime()
    g = generate_primitive_root(p)

    # Step 2: Alice chooses private key a
    a = random.randint(2, p - 2)

    # Step 3: Bob chooses private key b
    b = random.randint(2, p - 2)

    # Step 4: Calculate public keys
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)

    # Step 5: Exchange public keys
    shared_key_Alice = mod_exp(B, a, p)
    shared_key_Bob = mod_exp(A, b, p)

    # Both Alice and Bob now have the shared secret key
    return shared_key_Alice, shared_key_Bob, p, g

def main():
    shared_key_Alice, shared_key_Bob, prime, generator = diffie_hellman_key_exchange()

    print("Prime (p):", prime)
    print("Generator (g):", generator)
    print("Alice's shared key:", shared_key_Alice)
    print("Bob's shared key:", shared_key_Bob)

    assert shared_key_Alice == shared_key_Bob, "Key exchange unsuccessful!"
    

main()
