first=input()
first=first.split(' ')
space=int(first[0])
num=int(first[1])
inputs=[]
for i in range(num):
    inputs.append(int(input()))
remainders=[]
count=0
collide=False
for a in inputs:
    remainder=a%space
    count=count+1
    for other in remainders:
        if remainder==other:
            print(count)
            collide=True
            break
    if collide:
        break
    else:
        remainders.append(remainder)
if not collide:
    print(-1)