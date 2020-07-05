mystring1=input()
mystring2=mystring1.strip('[')
mystring3=mystring2.strip(']')
list1=mystring3.split(",")
list1=[int(x) for x in list1]
l=len(list1)
ss=[]
for i in range(l-1):
    s=0
    for j in range(i,l):
        if list1[i]>list1[j]:
            s=s+1
    ss.append(s) 
ss.append(0)    
print(ss)