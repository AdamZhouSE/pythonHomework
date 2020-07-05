a=eval(input())
temp=input().split(' ')
temp=map(eval,temp)
list1=list(temp)
result=[]
for i in range(a):
    temp=list1[i:]
    mini=min(temp)
    index=temp.index(mini)
    result.append(i+index+1)
    temp=temp[:index+1]
    temp.reverse()
    list1[i:i+index+1]=temp
for i in range(a):
    print(result[i],end=' ')