n,h = map(int,input().split(" "))
list1 = input().split(" ")
list1 = [int(list1[i]) for i in range(len(list1))]
result = 0
for j in list1:
    if j>h:
        result = result +2
    else:
        result = result +1
print(result)