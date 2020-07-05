l=input().split(' ')
l.pop()
l.reverse()
result=''
for n in l:
    result+=n+' '
print(result,end='')