#分块排序后再连接
#结果和原数组升序排列后相同
num=list(map(int,input().replace('[','').replace(']','').split(',')))
origin=[i for i in num] #543321
num.sort()  #123345
condition2=[i for i in num]
condition2.sort(reverse=True)

if origin==num:
    print(len(num))
elif origin==condition2:
    print(1)
else:
    start=0
    end=1
    count=0
    while end<=len(num):
        segment=origin[start:end]
        segment.sort()
        if segment==num[start:end]:
            start=end
            end=end+1
            count=count+1
        else:
            end=end+1
    print(count)



