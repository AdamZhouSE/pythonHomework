a=eval(input())

#print(a)

result=0

i=len(a)-1

first=0

while i>=0:
    if(a[i]==1):
        result=result+2**first
    
    first=first+1
    i=i-1
    
print(result)