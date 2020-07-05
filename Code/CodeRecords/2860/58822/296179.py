s1=int(input())
li=[]
for i in range(s1):
    s2 = input().split(' ')
    li.append(s2)
if(s1==2):
    if(li[0][0]==li[1][0] or li[0][1]==li[1][1]):
        print(0)
    else:
        print(1)
    exit()
sum=s1
for i in range(s1):
    for k in range(i+1,s1):
        if(li[i][0]==li[k][0] or li[i][1]==li[k][1]):
            sum-=1
print(sum-1)