number = int(input("Please enter a number : "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Number is not prime.")
            break
    else:
        print("Number is prime.")
else:
    print("Number is not prime.")