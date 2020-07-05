n=int(input())
s=input()
for i in range(n):
    tmp=input().split(' ')
    op=int(tmp[0])
    if(op==1):
        s=s+tmp[1]
        print(s)
    elif(op==2):
        s=s[int(tmp[1]):int(tmp[1])+int(tmp[2])]
        print(s)
    elif(op==3):
        s=s[:int(tmp[1])]+tmp[2]+s[int(tmp[1]):]
        print(s)
    elif(op==4):
        k=s.find(tmp[1])
        print(k)
