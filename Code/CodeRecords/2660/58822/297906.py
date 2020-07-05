num=int(input())
s=""
for i in range(num):
    ins=input().split(' ')
    if(ins[0]=='T'):
        s=s+ins[1]
    elif (ins[0]=='U'):
        k=int(ins[1])
        s=s[0:len(s)-k]
    else:
        k = int(ins[1])
        print(s[k-1])