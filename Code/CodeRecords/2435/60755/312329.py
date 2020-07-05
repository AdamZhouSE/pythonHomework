ex = input().split(" ")
all = []
num = []
for i in range(int(ex[0])):
    all.append(input())
for i in range(int(ex[1])):
    num.append(input().split(" "))
for i in num:
    temp = all[int(i[0])-1:int(i[1])]
    # print(temp)
    temp.sort()
    print(temp[-1])