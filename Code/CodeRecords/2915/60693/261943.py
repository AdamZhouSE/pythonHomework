def choose_questions(arr,n):
    arr.append(3000000000)
    maxlen=curlen=0
    break_point=-1
    for i in range(n):
        if arr[i]*2<arr[i+1]:
            curlen=i-break_point
            break_point=i
            if maxlen<curlen:maxlen=curlen
    # all the array can work
    return maxlen

n=int(input())
arr=list(map(int,input().split()))
res=choose_questions(arr,n)
print(res)