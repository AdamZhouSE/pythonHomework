n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
s1=0
s2=0
list1.sort(reverse=True)
for i in range(int(n/2.0+0.5)):
    s1+=list1[i]
for j in range(int(n/2.0+0.5),n) :
    s2+=list1[j]
print(s1*s1+s2*s2)

    
    

