string=input().split(" ")
string.reverse()
string.remove('0')
result=""
for i in range(len(string)):
    result=result+string[i]+" "
print(result,end='')