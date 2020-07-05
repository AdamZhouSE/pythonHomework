str = input()
result = []
big =len(str);
small = 0;
for i in range(0,len(str)):
    if str[i]=='I':
        result.append(small)
        small+=1
    else:
        result.append(big)
        big-=1

result.append(big)
print(result)