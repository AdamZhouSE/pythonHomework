n = int(input())
li = [int(x) for x in input().split()]
maxindex = li.index(max(li))
minindex = li.index(min(li))
print(max(abs(maxindex-minindex),maxindex,minindex,n-1-maxindex,n-1-minindex))