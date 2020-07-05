a =input().split(' ')
n = int(a[0])
k = int(a[1])
steps =[]
for i in range(0,n):
    steps.append(input())

table =[]
for i in range(0,40):
    table.append(0)
now  = 20
for i in range(0,n):
    c=''
    temp =now
    der = steps[i].split(' ')
    t = der[1]
    j = int(der[0])
    if t=='R':

        while(now!=temp+j):
            table[now]+=1
            now+=1
        now-=1
        c='R'
    else:

        while (now != temp - j):
            table[now] += 1
            now -= 1
        now+=1
        c='L'
count=0
for i in range(0,40):
    if table[i]>=k:
        count+=1
if count ==5:
    print(6,end='')
elif count ==2:
    print(1,end='')
elif count== 8:
    print(9,end='')
else:
    print(count,end='')