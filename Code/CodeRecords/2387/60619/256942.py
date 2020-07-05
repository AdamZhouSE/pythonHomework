def up_sort(s, e):
    while e > s:
        for i in range(e):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i+1]
                numbers[i+1] = numbers[i]
                numbers[i] = temp
        e -= 1


def down_sort(s, e):
    while e > s:
        k = e
        while k > s:
            if numbers[k] > numbers[k-1]:
                temp = numbers[k-1]
                numbers[k-1] = numbers[k]
                numbers[k] = temp
            k -= 1
        e -= 1


li = input().split(" ")
length = int(li[0])
t = int(li[1])
num = input().strip().split(" ")
numbers = [int(i) for i in num]
for ind in range(t):
    instru = input().strip().split(" ")
    startP = int(instru[1]) - 1
    endP = int(instru[2]) - 1
    if instru[0] == "0":
        up_sort(startP, endP)
    else:
        down_sort(startP, endP)
index = int(input())
print(numbers[index])