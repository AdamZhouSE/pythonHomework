num = eval(input())
for i in range(0,num):
    n = input()
    s=bin(int(n,10))[2:]
    li = list(s)
    for i in range(0,len(li)):
        if li[i]=='1':
            li[i]='0'
        else :
            li[i]='1'
    print(int(''.join(li),2))