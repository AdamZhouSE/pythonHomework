n=int(input())
a_i=input().split(' ')
ai=[]
ai.append(0)
for i in range(len(a_i)):
    ai.append(int(a_i[i]))
m=int(input())
count2=[]
for i in range(m):
    str1=input().split(' ')
    start=int(str1[0])
    end=int(str1[1])
    ai1=[]
    count=0
    for i in range(start,end+1):
        ai1.append(ai[i])
    for i in range(len(ai1)):
        for j in range(i+1,len(ai1)):
            if ai1[i]==ai1[j]:
                ai1[j]=0
    for i in range(len(ai1)):
        if ai1[i]!=0:
            count=count+1
    count2.append(count)
for i in range(len(count2)):
    print(count2[i])
    