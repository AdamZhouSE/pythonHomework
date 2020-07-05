num=int(input())
l=[]
l.append(num%2)
num=num//2
tag=0
while num>0:
    l.append(num%2)
    if l[-1]==l[-2]:
        print("False")
        tag=1
        break
    else:
        num=num//2
if tag==0:
    print("True")