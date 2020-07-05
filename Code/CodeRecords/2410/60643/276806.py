def solution(arr,diff)->int:
    max_len=0
    for i in range(len(arr)-1):
        temp=0
        for j in range(i+1,len(arr)):
            if arr[i]+diff==arr[j]:
                temp+=1
                i=j
                continue
        max_len=max(max_len,temp)
    return max_len+1


if __name__=="__main__":
    arr=eval(input())
    diff=int(input())
    ans=solution(arr,diff)
    print(ans)
