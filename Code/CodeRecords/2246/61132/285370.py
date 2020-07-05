import math

s=input()
Len=len(s)
Min=math.pow(10,Len-1)
Max=math.pow(10,Len)-1
i=0
while math.pow(2,i)<=Max:
    tmp = math.pow(2, i)
    if tmp>=Min:
        stmp=str(int(tmp))
        for j in set(list(stmp)):
            if str(int(tmp)).count(j)!=s.count(j):
                break
        else:
            print(True)
            break
    i+=1
else:
    print(False)