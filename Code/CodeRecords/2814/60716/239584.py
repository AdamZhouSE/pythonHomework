num = int(input())
str = input().split(' ')
needtime =[int(i) for i in str]
#print(needtime)
needtime.sort()
adder = 0
index=0
for i in needtime:
    if i>=adder:
        index+=1
        adder+=i
print(index)