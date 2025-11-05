n = int(input("Please enter the positive length : "))
num1 = 0
num2 = 1
print("Fabonacci Series:")
for i in range(n):
    print(num1)
    next_number = num1 + num2
    num1,num2 = num2,next_number