def count_num(array,number):
    result=0
    for i in range(len(array)):
        if number>array[i]:
            result=result+1
    return result
temp=input()
temp='['+temp+']'
D=eval(temp)
N=list(input())
N=N[::-1]
ans=0
N[0]=int(N[0])
for i in range(1,len(N)):
    ans=ans+int(pow(len(D),i))
    N[i]=int(N[i])
for i in range(1,len(N)):
    ans=ans+int(count_num(D,N[i])*pow(len(D),i))
print(ans)