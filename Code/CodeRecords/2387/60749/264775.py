n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
num_array=list(map(int,input().split(" ")))
ans=[]
for _ in range(m):
    temp=list(map(int,input().split(" ")))
    ans.append(temp)
q=int(input())
def judge(num_array,operate):
    if operate[0]==0:
        l=operate[1]-1
        r=operate[2]-1
        num_array=num_array[0:l]+sorted(num_array[l:r+1])+num_array[r+1:]
    else:
        l = operate[1] - 1
        r = operate[2] - 1
        num_array = num_array[0:l] + sorted(num_array[l:r + 1])[::-1] + num_array[r + 1:]
    return num_array
for h in ans:
    num_array=judge(num_array,h)
print(num_array[q-1])