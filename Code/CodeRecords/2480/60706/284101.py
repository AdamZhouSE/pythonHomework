t=int(input())
for i in range(t):
    n=int(input())
    str1=input().split(' ')
    odd=[]
    even=[]
    for i in range(n):
        if int(str1[i])%2==0:
            odd.append(int(str1[i]))
        else:
            even.append(int(str1[i]))
    ans=''
    for i  in range(len(odd)):
        ans=ans+str(odd[i])+' '
    for j in range(len(even)):
        ans=ans+str(even[j])+' '
    print(ans)
