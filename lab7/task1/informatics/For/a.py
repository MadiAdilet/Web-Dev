a = int(input())
b = int(input())
result = [str(i) for i in range(a, b + 1) if i % 2 == 0]
print(' '.join(result))