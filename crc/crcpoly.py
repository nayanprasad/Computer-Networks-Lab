def extract_coeficients(poly):
  powers = []
  print(poly.split(" + "))
  for term in poly.split(" + "):
    if term == "1":
      powers.append(0)
    if term == "x":
      powers.append(1)
    else:
      powers.append(int(term.split("^")[-1]))

  
  coefficients = []
  start = powers[0]
  end = powers[-1]
  
  print(powers)
  print(start, end)
  
  for i in range(end, start + 1):
    if(i in powers):
      coefficients.append("1")
    else:
      coefficients.append("0")
    
  coefficients.reverse()
  
  return "".join(coefficients)

def write_to_file(coefficients):
  with open("poly.txt", "w") as file:
    file.write(coefficients)
  file.close()


def main():
  poly = "x^8 + x^4 + x^3 + x^2 + x + 1"
  coeficineints = extract_coeficients(poly)
  print(coeficineints)
  write_to_file(coeficineints)
  
main()