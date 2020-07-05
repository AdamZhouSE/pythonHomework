def findBestValue(arr,target):
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        
        r, ans, diff = max(arr), 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans

    
info=input()[1:-1].split(',')
arr=[int(y) for y in info]
target=innt(input())
