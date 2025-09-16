input_str = input("")

result_str = ""
for char in input_str:
    if char.islower():
        result_str += char.upper()
    elif char.isupper():
        result_str += char.lower()
    else:
        result_str += char
print(result_str)