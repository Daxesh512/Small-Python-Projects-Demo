def fibonacci(n):
    if(n <= 0):
        print("Invalid Input.")
    elif(n ==1 or n==2):
        return n - 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number = int(input("Please enter the number:"))
print("Fibonacci number =",fibonacci(number))