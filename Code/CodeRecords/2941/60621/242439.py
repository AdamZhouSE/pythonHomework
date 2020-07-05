a=int(input())
b=input()
d={"A":4,"B":3,"C":2,"D":1,"F":0,"E":0}
c=0
for i in b:
    c+=d[i]
if(c==0):
    print(0,end="")
else:
    print("{:.14f}".format(c/len(b)),end="")