print("Give me a number: ", end="")
input_num = float(input())

if input_num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")