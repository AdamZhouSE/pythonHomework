seq=input()
p=[]
pre=''
for i in range(len(seq)):
    if(seq[i]=='P'):
        p.append(pre)
    elif(seq[i]=='B'):
        pre=pre[:len(pre)-1]
    else:
        pre+=seq[i]        
n=int(input())
for i in range(n):
    temp=[int(x) for x in input().split(' ')]
    x=temp[0]-1
    y=temp[1]-1
    print(p[y].count(p[x]))