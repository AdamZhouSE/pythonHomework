lst=eval(input())
sorted=lst.copy()
sorted.sort()
if lst.index(sorted[0])>lst.index(sorted[len(lst)-1]):print(1)
else:print(4)