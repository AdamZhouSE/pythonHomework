arr=eval(input())
s_arr=sorted(arr)
n=len(arr)
l=-1
num=0
for i in range(0,n):
    for j in range(l+1,i+1):
        if sorted(arr[l+1:j+1])==s_arr[l+1:j+1]:
            num+=1
            l=j
print(num)