def charReplace(s:str,k:int):
    if s==None:
        return 0
    strList = list(s)
    left,right,charMax = 0,0,0
    res = k
    map = [0]*26
    while right!=len(strList):
    #向右遍历
        map[ord(strList[right])-ord("A")]+=1
        #更新charmax
        charMax = max(charMax,map[ord(strList[right])-ord("A")])
        if(right-left+1>charMax+k):#长度过大 不能覆盖，移动left
            map[ord(strList[left])-ord('A')]-=1
            left+=1
        #update res
        #right - left +1是可以满足条件的窗口长度
        res = max(res,right-left+1)#如果是前面有了left右移的操作，这里不会更新的，因为res必定减少
        right+=1
    return res

s= input()
k = int(input())
print(charReplace(s,k))
