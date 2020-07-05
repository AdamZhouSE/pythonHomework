def pancakeSort(A):
        ans = []
        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1
        return ans
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
ans=pancakeSort(A)
num=0
for i in range(len(ans)):
    if ans[i]==1:
        num=num+1
for i in range(num):
    ans.remove(1)
print(ans)