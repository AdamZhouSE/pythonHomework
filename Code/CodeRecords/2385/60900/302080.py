n =int(input())
nums =[]
for i in range(0,n):
    nums.append(int(input()))

def check(a):
    b = a;
    while(a!=0):
        if a%2==1:
            if a==1:
                return 1
            a=int(a/2)
            if a%2==1:
                return 0
        else:
            a=int(a/2)

    return 1

for i in range(0,n):
    result=0
    for j in range(0,2**nums[i]):
        result+=check(j)
    print(result)