str=input().split()
max=str[0]
for i in range(0,len(str)):
    if len(str[i])>len(max):
        max=str[i]
print(max)