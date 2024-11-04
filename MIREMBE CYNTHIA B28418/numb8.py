def gcd(m, n):
    while m != 0:
        m, n = n % m, m
    return n

# Get user input
try:
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))

    if num1 <= 0 or num2 <= 0:
        print("Please enter positive integers.")
    else:
        result = gcd(num1, num2)
        print(f"The GCD of {num1} and {num2} is: {result}")
except ValueError:
    print("Please enter valid integers.")
