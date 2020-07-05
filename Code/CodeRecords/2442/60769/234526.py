a = input().rstrip(']').lstrip('[').split(",")
l = list(map(int,sorted(a)))
max = 0
temp = 0
for i in l:
    res = i-temp
    temp = i
    if res>max:
        max = res
print(max)