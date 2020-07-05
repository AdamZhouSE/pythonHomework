people_num = int(input())
info = [[i] for i in range(0, people_num)]
a = list(map(int, input().split()))
a = [x - 1 for x in a]
count = 0
flag = True
print(a)