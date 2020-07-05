def minSwapsCouples(row):
    l = len(row)
    ans = 0
    for i in range(0,l-1,2):
        if(row[i]%2 == 0):
            temp = row[i] + 1
        else:
            temp = row[i] - 1
        if temp == row[i+1]:
            continue
        for j in range(i+2,l,1):
            if row[j]==temp:
                row[i+1],row[j] = row[j],row[i+1]
                ans+=1
                break
    return ans

nums = list(map(int,input()[1:-1].split(", ")))
print(minSwapsCouples(nums))
