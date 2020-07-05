n,d=list(map(int,input().split()))
arr=list(map(int,input().split()))
sorted_arr=sorted(arr)
counter=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if(abs(sorted_arr[i]-sorted_arr[j])<=d):
            counter+=1
        else:
            break
print(counter*2)