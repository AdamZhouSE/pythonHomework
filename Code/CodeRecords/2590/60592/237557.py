total = int(input())
data = []
for i in range(0,total):
    ls = input()
    data.append(ls)
for i in range(0,total):
    sum = 0
    ss = list(set(data[i]))
    tem = [0]*len(ss)
    for h in range(0,len(ss)):
        for j in range(0,len(data[i])):
            if data[i][j] == ss[h]:
                tem[h]+=1
    for h in range(0,len(ss)):
        if tem[h] == 1:
            sum+=1
    if sum%2==1:
        print("HE!")
    else:
        print("SHE!")
    