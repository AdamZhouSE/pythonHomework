def so(li):
    index = -1
    for i in range(0,len(li)):
        if li[i] == '1' and index==-1:
            index = i
            continue
        if li[i]=='1' and index!=-1:
            return -1
    if index ==0:
        index = 2
    return index;
        
num  =eval(input())
for i in range(0,num):
    n = input()
    s=bin(int(n,10))[2:]
    li = list(s)
    print(so(li))