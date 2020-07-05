inte=int(input())
exp=True

while(True):
    if(inte==1):
        break
    elif(not(inte%2==0)):
        exp=False
        break
    else:
        inte=inte/2

print(exp)