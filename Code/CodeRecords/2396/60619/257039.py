def find_min(start):
    result = start
    curr = numbers[start]
    for i in range(start+1, length):
        if numbers[i] < curr:
            curr = numbers[i]
            result = i
    return result


def exchange(start, end):
    while start < end:
        temp = numbers[end]
        numbers[end] = numbers[start]
        numbers[start] = temp
        start += 1
        end -= 1


length = int(input())
num = input().split(" ")
numbers = [int(i) for i in num]
for i in range(length):
    min_id = find_min(i)
    print(min_id + 1, end=" ")
    exchange(i, min_id)
