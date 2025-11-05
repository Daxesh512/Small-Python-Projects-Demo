n = int(input("Please enter a positive number : "))
def is_Perfect_Square(n):
    s = int(n ** 0.5)
    return s*s == n
if (is_Perfect_Square(5*n*n+4) or is_Perfect_Square(5*n*n-4)):
    print(n, "is fibanacci.")
else:
    print(n, "is not fibanacci.")