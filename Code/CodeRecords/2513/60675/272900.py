def func(n : list, index : int) -> int :
    list = n
    list.sort()
    answer = 0
    for i in range(index):
        answer = list[i]
    return answer
        
num = int(input())
l = []
for i in range(num):
    n = input().split(",")
    for j in range(len(n)):
        l.append(int(n[j]))
index = int(input())
print(func(l,index))