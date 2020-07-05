numAndIniti =input().split()

NUM=int(numAndIniti[0])
initi=int(numAndIniti[1])

chapters=list(map(int,input().split()))
chapters.sort()

result=0;
if initi>NUM:
    for i in chapters:
        result+=i*initi
        initi-=1
else:
    for i in chapters:
        if initi>1:
            result+=i*initi
            initi-=1
        else:
            result+=i
print(result)



