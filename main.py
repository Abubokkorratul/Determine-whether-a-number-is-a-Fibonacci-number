n = int(input("Enter a number: "))
a, b = 0, 1
is_fibonacci = False
while a <= n:
    if a == n:
        is_fibonacci = True
        break
    a, b = b, a + b
if is_fibonacci:
    print(f"{n} is a Fibonacci number")
else:
    print(f"{n} is not a Fibonacci number")
