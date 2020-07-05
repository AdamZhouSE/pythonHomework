import sys
days=int(input())
count=[]
for i in range(days):
    count.append(int(input()))
wave=count[0]
for i in range(1,days):
    minimum = sys.maxsize
    for j in range(0,i):
        a=abs(count[j]-count[i])
        if a<minimum:
            minimum=a
    wave+=minimum
print(wave,end="")