def listSum(a):
    answer=0
    for i in a:
        answer+=i
    return answer


n=int(input())
num=input().split()
num=[int(x) for x in num]
answer=0
for i in range(n-1):
    for j in range(i,n):
        if listSum(num[0:i])==listSum(num[i:j]) and listSum(num[i:j])==listSum(num[j:n]):
            answer+=1
print(answer)