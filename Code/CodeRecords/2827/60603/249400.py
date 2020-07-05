str=int(input())
sta=input().split(" ")
for i in range(len(sta)):
    sta[i]=int(sta[i])
sta.sort()
for i in range(len(sta)):
    if (i==(len(sta)-1)):
        print(sta[i])
    else:
        print(sta[i],end=" ")