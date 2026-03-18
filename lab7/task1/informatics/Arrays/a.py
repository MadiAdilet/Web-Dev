n = int(input())                
numbers = input().split()       
result = []                    

for i in range(n):              
    if i % 2 == 0:              
        result.append(numbers[i]) 

print(' '.join(result))          