x = input()  
reversed_str = ''
for digit in reversed(x):
    reversed_str += digit
print(int(reversed_str))  