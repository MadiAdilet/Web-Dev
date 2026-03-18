#1
def sleep_in(weekday, vacation):
    return (not weekday) or vacation
#2
def string_times(str, n):
    return str * n
#3
def first_two(str):
    return str[:2]
#4
def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i+2] == "hi":
            count += 1
    return count
#5
def max_end3(nums):
    max_val = max(nums[0], nums[2])
    return [max_val, max_val, max_val]
#6
def sum67(nums):
    total = 0
    skip = False
    for num in nums:
        if num == 6:
            skip = True
        elif not skip:
            total += num
        elif num == 7:
            skip = False
    return total