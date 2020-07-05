mystring1=input()
mystring2=mystring1.strip('[')
mystring3=mystring2.strip(']')
list1=mystring3.split(",")
list1=[int(x) for x in list1]
l=len(list1)
low=int(input())
upper=int(input())
sm=0

for i in range(l):
    for j in range(i,l):
        ss=0
        if i==j and list1[i]>=low and list1[i]<=upper:
            sm=sm+1
        else:
            for p in range(i,j+1):
                ss=ss+list1[p]            
            if ss>=low and ss<=upper:
                sm=sm+1
print(sm)   