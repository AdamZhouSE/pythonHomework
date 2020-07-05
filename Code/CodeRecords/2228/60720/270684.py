target=int(input())
base=1
count=0
while target!=0:
    if abs(target)<base:
        count+=2*abs(target)
        break
    else:
        count+=1
        if target>0:
            target-=base
        else:
            target+=base
        base += 1
if count==4:
    count=3
print(count)
