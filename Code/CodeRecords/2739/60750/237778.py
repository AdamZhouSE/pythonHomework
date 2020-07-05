def sum(k,n):
    res = []

    def back(num,now,temp,next_sum):
        '''num:已使用的数字数，now：当前数字，temp：当前中间结果，next_sum：剩余数字和'''
        if num == k:
            if next_sum == 0:
                res.append(temp)
                return
        for i in range(now,10):
            if i > next_sum:
                break
            back(num + 1,i + 1,temp + [i],next_sum - i)

    back(0,1,[],n)
    return res


a = input().split(',')
k = int(a[0])
n = int(a[1])
print(sum(k,n))