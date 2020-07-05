num = int(input())

def isPerfect(num):
    arr = []
    for i in range(1, num):
        if num % i == 0:
            arr.append(i)
    total = sum(arr)
    return total == num

print(isPerfect(num))