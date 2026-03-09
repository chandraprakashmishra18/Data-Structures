# find some of odd digits in a given user number
num  = input("Enter your number: ")
new_no = 0
for digit in num:
    n = int(digit)
    if n%2!=0:
        new_no += n
print(new_no) 

