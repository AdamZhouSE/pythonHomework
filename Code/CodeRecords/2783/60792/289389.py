num=int(input())
dic={}
for i in range(0,num):
    s,n=input().strip().split(" ")
    n=int(n)
    if not (s in dic):
        dic[s]=n
    else:        
        temp=dic[s]+n
        del dic[s]
        dic[s]=temp
s1=""
maxscore=0
for i,j in dic.items():
    if j>maxscore:
        maxscore=j
        s1=i
print(s1)
