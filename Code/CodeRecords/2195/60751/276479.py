import math

num=int(input())
def change(num):
    result=""
    while(num>0):
        result=str(num%2)+result
        num//=2
    return result
def is_(num):
    count=0
    for i in num:
        if i=="1":
            count+=1
    if count==1:
        return True
    a = False
    ed = int(str(math.sqrt(int(count))).split(".")[0])
    for i in range(2, ed + 1):
        if int(count) % i == 0:
            a = True
            break
    return a
for i in range(num):
    l=input().split(" ")
    L=int(l[0])
    R=int(l[1])
    count=0
    for j in range(L,R+1):
        if not is_(change(j)):
            #print(j)
            #print(change(j))
            count+=1
    print(count)