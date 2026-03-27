<<<<<<< HEAD
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

x = int(input("Enter a non-negative integer: "))
factorial_of_x = factorial(x)
=======
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

x = int(input("Enter a non-negative integer: "))
factorial_of_x = factorial(x)
>>>>>>> ed2f51ce4940f185166ddd19bbe02f7be81f4ba2
print(f"The factorial of {x} is {factorial_of_x}")