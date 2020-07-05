import math
a=float(input())
n=int(input())
alist=str(round(math.pow(a,n),5)).split('.')
alist[1] = alist[1] if len(alist[1])==5 else alist[1]+"".join(['0' for i in range(5-len(alist[1]))])
print(".".join(alist))