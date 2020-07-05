n=int(input())
Sum=0
l=[]
while n!=0:
    two=''.join(map(lambda x:'1'if x!='0'else'0',list(str(n))))
    n-=int(two)
    l.append(two)
    Sum+=1
print(Sum)
print(' '.join(l))