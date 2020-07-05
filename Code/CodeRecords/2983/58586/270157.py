num=int(input())
used=[]
try:
    while True:
        temp=input()
        if temp!="":
            arr=[c for c in temp]
            for i in arr:
                if i not in used:
                    used.append(i)
                else:
                    used.remove(i)
            if len(used)>1:
                print("Impossible")
            else:
                left=0
                right=len(arr)-1
                count=0
                while left<right:
                    if arr[left] != arr[right]:
                        idx=right
                        while arr[idx]!=arr[left] and idx>left:
                            idx-=1
                        if idx==left:
                            count+=len(arr)//2-left
                            left+=1
                            continue
                        count+=right-idx
                        for i in range(idx,right):
                            arr[i],arr[i+1]=arr[i+1],arr[i]
                    left += 1
                    right -= 1
                print(count)
except EOFError:
    pass