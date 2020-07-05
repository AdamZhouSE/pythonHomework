n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list2=input().split()
list2=[int(x) for x in list2]
n01=list1[0]
n02=list2[0]
sum=0
while(n01>0 and n02>0):
    n1=list1[1]
    n2=list2[1]
    sum+=1
    if n1>n2:
        list1.append(n2)
        list1.append(n1)
        n01+=1
        list1[0]=n01
        
        del list1[1] 
        del list2[1]
        n02-=1
        list2[0]=n02
    else:
        list2.append(n1)
        list2.append(n2)
        n02+=1
        list2[0]=n02
        del list1[1] 
        del list2[1]
        n01-=1
        list1[0]=n01
    if sum>100:
        print("-1")
        break
if n01==0:
    print(str(sum)+" "+"2")
elif n02==0:
    print(str(sum)+" "+"1")
        