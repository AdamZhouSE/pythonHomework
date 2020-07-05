a=int(input())
b=int(input())
judge=True
time=0
while(judge):
    if a*2<b:
        a=a*2
        time+=1
        continue
    elif a-1==b:
        time+=1
        break
    elif a*2==b:
        time+=1
        break
    elif a*2-1>b:
        a-=1
        time+=1
        continue
    elif a*2-1==b:
        a*=2
        time+=1
        continue
print(time)