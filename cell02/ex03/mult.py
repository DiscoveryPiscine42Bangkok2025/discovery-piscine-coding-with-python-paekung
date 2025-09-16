print("Enter first number:")
num1 = int(input())
print("Enter second number:")
num2 = int(input())

ans = num1 * num2
print(f"{num1} x {num2} = {ans}")

if ans < 0:
    print("The result is negative.")
elif ans == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")