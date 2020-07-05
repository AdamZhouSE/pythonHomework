m = int(input())
n = input().split(" ")
list = []
for i in n:
    if i not in list and i != "0":
        list.append(i)
print(len(list))
