n=int(input())
line=sorted([int(i) for i in input().split()])
wait=0
num=0
for i in line:
    if wait<=i:
        num+=1
        wait+=i
print(num)