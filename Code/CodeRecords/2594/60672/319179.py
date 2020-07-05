def repeat(arr):
    length=-1
    midlen=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]==arr[i]:
                midlen=j-i-1
            length=max(length,midlen)
    return length
t=int(input())
for i in range(t):
    string=input()
    answer=repeat(string)
    print(answer)