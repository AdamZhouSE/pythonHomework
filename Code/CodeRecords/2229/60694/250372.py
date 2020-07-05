arr = list(map(int, input().split(",")))
cnt1, cnt2 = 0, 0
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        cnt2 += 1
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            cnt1 += 1
if cnt1 == cnt2:
    print("True")
else:
    print("False")
