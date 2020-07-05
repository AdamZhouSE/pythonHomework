target = abs(int(input()))
index = 1
while True:
    temp = index*(index+1)//2
    if temp-target>=0 and (temp-target)%2==0 and (temp-target)%2<index:
        print(index+1)
        break
    index+=1