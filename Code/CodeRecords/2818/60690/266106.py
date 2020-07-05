in1=input().split(" ")
chapters=input().split(" ")
Time=int(in1[1])

for i in range(len(chapters)):
    chapters[i]=int(chapters[i])

chapters.sort()
res=0

for i in range(len(chapters)):
    if Time>1:
        res+=Time*int(chapters[i])
        Time-=1
    else:
        res+=int(chapters[i])

print(res)