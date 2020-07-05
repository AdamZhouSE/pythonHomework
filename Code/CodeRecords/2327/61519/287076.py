s=list(input())
number=0
length=len(s)
result=[]
for string in s:
    if string=='I':
        result.append(number)
        number+=1
    else:
        result.append(length)
        length-=1
result.append(length)
print(result)