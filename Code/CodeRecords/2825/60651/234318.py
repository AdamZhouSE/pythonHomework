n=int(input())
list2=[]

for i in range(n):
    sum=0
    list1=input().split()
    list1=[int(x) for x in list1]
    for j in list1:
        sum+=j
    list2.append(sum)
s1=list2[0] 

list2.sort(reverse=True)

for i in range(n):
    if s1==list2[i]:
        print(i+1)
        break
    
    