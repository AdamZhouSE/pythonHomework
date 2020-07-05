n = int(input())
all = []
word = []
for i in range(n):
    all.append((input().split(" "))[1:])
m = int(input())
for i in range(m):
    word.append(input())
for i in word:
    temp = ""
    for k in range(len(all)):
        if i in all[k]:
            temp = temp + str(k+1)+" "
    if len(temp)!=0:
        print(temp)
    else:
        print(" ")
    