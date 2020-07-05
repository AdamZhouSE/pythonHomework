m = int(input())
n = input().split(" ")
list = []
for i in n:
    if i not in list:
        list.append(i)
print(len(list))
