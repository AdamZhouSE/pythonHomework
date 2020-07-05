def find(numbers,i,sum):
    if i==len(numbers)-1:
        return (sum+numbers[i])%360==0 or (sum-numbers[i])%360==0
    else:
        return find(numbers,i+1,sum+numbers[i]) or find(numbers,i+1,sum-numbers[i])

n=int(input())
numbers=[]
for i in range(0,n):
    numbers.append(int(input()))
if find(numbers,0,0):
    print("YES")
else:
    print("NO")