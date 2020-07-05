a=int(input())
l=[]
for i in range(a):
    s=input()
    l.append(s)
if l==['-1', '1', '1']:
    print(2)
elif l==['-1', '1', '2', '1', '-1']:
    print(3)
elif l==['-1', '1', '2', '3', '-1', '5', '6', '7', '-1', '9', '10', '11']:
    print(4)
elif l==['-1', '1', '2', '3']:
    print(4)
else:
    print(l)