list1=input().split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
ans=""
for i in range(23,-1,-1):
    for j in range(59,-1,-1):
        tmp = [int(m) for m in str(i)] + [int(n) for n in str(j)]
        while len(tmp) < 4:
            tmp.append(0)
        if sorted(tmp) == sorted(A):
            ans=str(i).zfill(2) + ':' + str(j).zfill(2)
print(ans)