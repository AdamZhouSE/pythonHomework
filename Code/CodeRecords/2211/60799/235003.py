list = input().split()
n = int(list[0])
k = int(list[1])
list.clear()
for i in range(0, n):
    list.append("")
    tmp = input().split()
    list[i] = tmp[0] + list[int(tmp[1])-1]
for i in range(0, k):
    start = input()
    print(len([word for word in list if word.startswith(start)]))