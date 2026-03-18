#1
n = int(input())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
#2
print("Hello, World!")
#3
n = int(input())
for i in range(n):
    print(i * i)
#4
n = int(input())
for i in range(1, n + 1):
    print(i, end='')
#5
n = int(input())
lst = []
for _ in range(n):
    command = input().split()
    if command[0] == "insert":
        lst.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(lst)
    elif command[0] == "remove":
        lst.remove(int(command[1]))
    elif command[0] == "append":
        lst.append(int(command[1]))
    elif command[0] == "sort":
        lst.sort()
    elif command[0] == "pop":
        lst.pop()
    elif command[0] == "reverse":
        lst.reverse()
#6
a = int(input())
b = int(input())
print(a // b)
print(a / b)
#7
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(coordinates)
#8
n = int(input())
arr = list(map(int, input().split()))
unique_scores = sorted(set(arr), reverse=True)
print(unique_scores[1])
#9
n = int(input())
students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted(set([student[1] for student in students]))
second_lowest = grades[1]  

names = [student[0] for student in students if student[1] == second_lowest]
names.sort()

for name in names:
    print(name)
#10
n = int(input())
students = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    students[name] = marks

query = input()
marks = students[query]
average = sum(marks) / len(marks)
print("{:.2f}".format(average))