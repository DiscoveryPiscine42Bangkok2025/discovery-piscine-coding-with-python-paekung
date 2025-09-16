print("Enter a number less than 25")
num = int(input())
if num < 25:
    for i in range(num, 26):
        print(f"Inside the loop, my variable is " + f"{i}")
else:
    print("Error")