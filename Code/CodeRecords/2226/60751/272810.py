left=int(input())
right=int(input())
def judgment(num):
    a=1
    for i in str(num):
        if int(i)==0 or num%int(i)!=0:
            a=0
            break
    if a==1:
        return True
    else:
        return False
l=[]
for i in range(left,right+1):
    if judgment(i):
        l.append(i)
print(l)
