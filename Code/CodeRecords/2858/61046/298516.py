def max(i,j):
    if i==1 or j==1:
        return 1
    if i==2:
        return j
    else:
        return max(i-1,j)+max(i,j-1)

num=int(input())
print(max(num,num))