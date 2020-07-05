res=input().split(',')
i=0
j=0
flag=False
leng=len(res)
part1=0
part2=0
part3=0
while i<leng :
    part1=int("".join(res[:i+1]),2)
    j=i+1
    while j<leng-1:
        part2=int("".join(res[i+1:j+1]),2)
        part3 = int("".join(res[j+1:]), 2)
        if(part2==part3==part1):
            flag=True
            break
        j+=1
    if(flag):
        break
    i+=1
if(flag):
    print([i,j+1])
else:
    print([-1,-1])