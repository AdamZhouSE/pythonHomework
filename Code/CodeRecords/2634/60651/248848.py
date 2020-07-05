mystring1=input()
mystring2=mystring1.strip('[')
mystring3=mystring2.strip(']')
list1=mystring3.split(",")
list1=[int(x) for x in list1]
n=int(input())
l=len(list1)
list2=[]
for i in range(l):
    for j in range(l):
        if list1[i]<list1[j]:
            list2.append(list1[i]/list1[j])
            list2.sort();
            
            if list2.index(list1[i]/list1[j])==n-1:
                si=list1[i]
                sj=list1[j]
list3=[si,sj]
print(list3)
