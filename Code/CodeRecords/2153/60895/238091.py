a=input()
b=int(a)
c=a.strip('-')
temp=c[::-1]
result=temp.lstrip('0')
if b<0:
    result='-'+result
print(result)   
        