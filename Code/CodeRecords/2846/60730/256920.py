m = int(input())
n = map(int, input().split())
n = {}.fromkeys(n).keys()            #几种删除方法
condition = lambda t: t != 0
filter_list = list(filter(condition, n))        #lambda 筛选方法
print(len(filter_list))
