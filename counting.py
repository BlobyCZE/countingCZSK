# +
def add(num1, num2):
    return num1 + num2
# -
def subtract(num1 , num2):
  return num1 - num2
# *
def multiply(num1, num2):
   return num1 * num2
# /
def divide(num1, num2):
   return num1 / num2
# //
def integer_divide(num1 , num2):
   return num1 // num2
# %
def modulo(num1, num2):
   return num1 % num2

# Nějaký příklad
num1 = float(input('ZADEJ SEM SVŮJ PŘÍKLAD:'))
num2 = float(input('ZADEJ SEM SVŮJ PŘÍKLAD:'))

# Printy
print("+:", add(num1, num2)) # Plus jsou jako třeba num1+num2
print("-:", subtract(num1, num2)) # Mínus = num1-num2
print("*:", multiply(num1, num2))
print("/:", divide(num1, num2))
print("//:", integer_divide(num1, num2))
print("%", modulo(num1, num2))
print("Vytvořil s láskou BlobyCZ | https://github.com/blobycze/pocitadlo")
