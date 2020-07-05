nm=input().split(' ')
n,m=int(nm[0]),int(nm[1])
dic=[]
for i in range(n):
    dic.append(input())
for j in range(m):
    se=input().split(' ')
    s,e=int(se[0])-1,int(se[1])-1
    temp=dic[s:e+1]
    temp.sort(reverse=True)
    print(temp[0])