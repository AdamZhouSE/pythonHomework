m = int(input())
n = map(int, input().split())
n = {}.fromkeys(n).keys()            #几种删除方法
n.remove(0)
print(len(n))