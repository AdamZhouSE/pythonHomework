n=int(input())
list1=[]
sum=1
list2=[]
for i in range(n):
    list1=list(input())
    l=len(list1)
    list1=[int(ord(x)) for x in list1]
    list1.sort()

    if list1[0]==32: 
        del(list1[0])
    
    list1=[chr(x) for x in list1]


    st="".join(list1)

    st.replace(' ','')
    list2.append(st)
set1= set(list2)
print(str(len(set1)),end="")

    