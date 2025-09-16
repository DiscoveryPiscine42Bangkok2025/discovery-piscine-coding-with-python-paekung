# The program accepts user input. This input is a number, which you will store in a
# numeric variable.
# • This number represents the multiplication table you will display. (For example, if
# the input is 2, you need to display the table for 2)

print("Enter a number")
num = int(input())
for i in range(0, 10):
    ans = num * i
    print(f"{i} x {num} = {ans}")