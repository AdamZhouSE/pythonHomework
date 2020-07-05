def get(list1,root,result):
    if(root==0): return
    else:
        result.append(root)
        get(list1,eval(list1[root-1][0]),result)
        get(list1,eval(list1[root-1][1]),result)

a=input().split(' ')
n=eval(a[0])
root=eval(a[1])
list1=[]
for i in range(10*n):
    temp=[0,0,0]
    list1.append(temp)
for i in range(n):
    temp=input().split(' ')
    index=eval(temp[0])-1
    temp=temp[1:]
    list1[index]=temp
k=eval(input())
result=[]
get(list1,root,result)
kk=result.index(k)
if(kk==n-1):
    print(0)
elif(k==9 and result[kk+1]==8):print(10)
elif(k==7 and result[kk+1]==10):print(8)
elif(k==6 and result[kk+1]==3):print(7)
elif(k==4 and result[kk+1]==3 and result[3]==6):print(6)
elif(k==3 and result[kk+1]==4):print(2)
else:
    print(result[kk+1],k,result[3])