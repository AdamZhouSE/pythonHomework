n=int(input())
name=[]
result=''
while(n>0):
    n -= 1
    new=input()
    if new in name:
        result += 'YES\n'
    else:
        result += 'NO\n'
    name.append(new)
print(result,end='')