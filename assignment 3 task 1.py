def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("Enter a positive number: "))
print(f"factorial of {n} is " ,fact(n))