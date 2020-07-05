str=input()
l=str.split('+')
l.sort()
result=''
for num in l:
    result=result+num+'+'
print(result[:-1])