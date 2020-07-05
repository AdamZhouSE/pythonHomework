mystring1=input()
mystring2=mystring1.strip('[')
mystring3=mystring2.strip(']')
list1=mystring3.split(",")
list1=[int(x) for x in list1]
n=len(list1)
k=int(input())
list1.sort()
dis=0
list2=[]
for i in range(n-1):
    for j in range(i+1,n):
        dis=list1[j]-list1[i]
        list2.append(dis)
        
list2.sort()
print(list2[k-1])
        
        