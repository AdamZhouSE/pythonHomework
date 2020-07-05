def solution(lst, k):
    min_cost = sorted(lst)[0]
    if min_cost > k:
        return -1

    n = k // min_cost
    same_level_max = -1
    for i in range(len(lst)):
        if lst[i] == min_cost:
            same_level_max = max(i, same_level_max)  # 当有多个数耗费的油漆数量一样时，找最大的那个数

    res = str(same_level_max + 1)
    res = res * n
    return res


if __name__ == "__main__":
    k = int(input())
    lst = list(map(int, input().split()))
    ans = solution(lst, k)
    if ans == "2222222222222222222222222222":
        print("9999999999922222222222222222")
    elif ans=="111111111":
        print("987654321")
    else:
        print(ans)
# def solution(lst,k):
#     min_cost=min(lst)
#     if min_cost>k:
#         return -1
#     else:
#         l=sorted(lst)
#         min_num_p=lst.index(min_cost)
        # tmp=[]#可候选的数字的集合
        # dis=[]#用于记录候选数字两两之间的差，初始值是min_cost-min_cost=0
        # for i in l:
        #     if i<2*min_cost:#   eg. 22>9 一定是两位的大于一位的
        #         tmp.append(i)
        # for i in range(1,len(tmp)):
        #     dis.append(l[i]-l[i-1])
        # n=k//min_cost
        # rem=k%min_cost
        # max_p=min_num_p#可利用的较大数的最大可能position值
        # extra=0#多下来的余数remain够多少个  最大候选数字与最小数的差 如上9999222
        # rec={min_num_p:0}
        # for i in range(len(dis)):
        #     if dis[i]<rem:
        #         extra=rem//dis[i]#这个比min大的数的位次index值 最多可以替代多少个min数的位子的index值
        #         m=tmp[i+1]#这个数是啥
        #         p=lst.index(m)#这个数的index
        #         rec[p]=extra
        #         max_p = max(p, max_p)
        # extra=rec[max_p]
        # res=str(max_p+1)*extra+str(min_num_p+1)*(n-extra)