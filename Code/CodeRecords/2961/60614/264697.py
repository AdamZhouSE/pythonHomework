str=input()
all=[]
for i in range(len(str)):
    all.append(str[i:]+str[0:i])
all.sort()
result=''
for i in all:
    result+=i[-1]
print(result,end='')