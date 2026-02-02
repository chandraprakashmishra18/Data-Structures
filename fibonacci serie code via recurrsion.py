def fib(n):
    if n <=0 :
        return "Invalid Input"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

num = int(input("Enter a positive integer: "))
for n in range(1, num+1):
    print(f"The {n}th Fibonacci number is: {fib(n)}")
    print(fib(num))
    

