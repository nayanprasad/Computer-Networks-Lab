import random
import math

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(math.sqrt(num) + 1)):
    if num % i == 0:
      return False
  return True
    
def generate_prime():
  while True:
    p = random.randint(2**10, 2**15)
    if is_prime(p):
      return p  

def is_primitive_root(g, p):
  for i in range(1, p-1):
    if pow(g, i, p) == 1:
      return False
  return True
  
def generate_primitive_root(p):
  while True:
    g = random.randint(2, p-1)
    if is_primitive_root(g, p):
      return g
    
def mode_exp(base, exponent, mod):
  result = 1
  base = base % mod  # reduce base
  while exponent > 0:
    if exponent % 2 == 1:  # exponent is odd
      result = (result * base) % mod # multiply result with base and reduce it
    exponent //= 2 
    base = (base * base) % mod 
  return result

def diffi_exchange():
  p = generate_prime()
  g = generate_primitive_root(p)
  
  xa = random.randint(2, p-1)  
  xb = random.randint(2, p-1)
  
  ya = mode_exp(g, xa, p)
  yb = mode_exp(g, xb, p)
  
  ka = mode_exp(yb, xa, p)
  kb = mode_exp(ya, xb, p)
  
  is_equal = ka == kb
  
  return p, g, xa, xb, ya, yb, ka, kb, is_equal
  
def main():
  p, g, xa, xb, ya, yb, ka, kb, is_equal = diffi_exchange()
  print("p:", p)
  print("g:", g)
  print("xa:", xa)
  print("xb:", xb)
  print("ya:", ya)
  print("yb:", yb)
  print("ka:", ka)
  print("kb:", kb)
  print("is_equal:", is_equal)
  
main()