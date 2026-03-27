<<<<<<< HEAD
def fib(n):
    if n <=0 :
        return "Invalid Input"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter a positive integer: "))
for i in range(1, n+1):
    print(f"The {i}th Fibonacci number is: {fib(i)}")
=======
def fib(n):
    if n <=0 :
        return "Invalid Input"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter a positive integer: "))
for i in range(1, n+1):
    print(f"The {i}th Fibonacci number is: {fib(i)}")
>>>>>>> ed2f51ce4940f185166ddd19bbe02f7be81f4ba2
