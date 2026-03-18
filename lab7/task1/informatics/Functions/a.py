def min(a, b, c, d):
    m = a
    if b < m:
        m = b
    if c < m:
        m = c
    if d < m:
        m = d
    return m


numbers = list(map(int, input().split()))
result = min(numbers[0], numbers[1], numbers[2], numbers[3])
print(result)