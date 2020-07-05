n=int(input())
list1=input().split(' ')
list2=input().split(' ')
sub=int(list2[1])-int(list2[0])
ans=int(0)
for i in range(int(list2[0])-1,int(list2[0])+sub-1):
    ans=ans+int(list1[i])
print(ans)