import sys
list=sys.stdin.readline().split(",")
maxlen=1
length=len(list)
for i in range(0,length-1):
    current=int(list[i])
    len=1
    for j in range(i+1,length):
        if int(list[j])>current:
            len+=1
            current=int(list[j])
    if len>maxlen:
        maxlen=len
print(maxlen)