a=input()
b=[]
for i in a:
    b.append(int(i))
a=int(a)
ans=""
leng=0
while a>0:
    temp=""
    for i in range(len(b)):
        if b[i]>0:
            temp+="1"
            b[i]-=1
            a-=10**(len(b)-i-1)

        else:
            temp+="0"
    leng += 1
    ans+=(str(int(temp))+" ")
print(leng)
print(ans.rstrip())
