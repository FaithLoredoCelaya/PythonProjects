n = int(input("Enter how many times you want to do this: "))
if n <1:
    print("N must be greater than 1")
if n>100:
    print("Too much work, no thanks")
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)