n=int(input())
a=int(input())
b=int(input())
result=[]
def div(n):
    if(n%a==0 or n%b==0):
        return True
    return False
x=min(a,b)
while True:    
    if(div(x)):
        result.append(x)    
    if(len(result)==n):
        break
    x+=1    
print(result[-1])