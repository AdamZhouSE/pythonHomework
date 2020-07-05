l = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
num = 0
need = []
for i in range(l):
    if arr[i] == 0:
        if 0 < i < l - 1:
            if arr[i - 1] == 1 and arr[i + 1] == 1:
                need.append(i)
count = 0
for i in range(len(need)):
    if i > 0:
        if need[i] - need[i-1] == 2:
            need[i] = 0
            count += 1
print(len(need) - count)