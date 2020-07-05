import sys
num=int(sys.stdin.readline())
list=sys.stdin.readline().split(",")
jud=False
length=len(list)
for len in range(1,len(list)+1):
    for start in range(0,length-len+1):
        sum=0
        for i in range(start,start+len):
            sum+=int(list[i])
        if sum>=num:
            print(len)
            jud=True
            break
    if jud:
        break