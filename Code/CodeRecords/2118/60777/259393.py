n=int(input())
exp=True
while(True):
    if(n==0):
        exp=False
        break
    if(n==1):
        break
    elif(n%3!=0):
        exp=False
        break
    else:
        n=n/3

print(exp)