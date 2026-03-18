a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = []
for x in range(a, b + 1):
    if x % d == c:
        result.append(str(x))

print(' '.join(result))