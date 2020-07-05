n=int(input())
Sum=0
while n!=0:
    two=''.join(map(lambda x:'1'if x!='0'else'0',list(str(n))))
    n-=int(two)
    Sum+=1
print(Sum)