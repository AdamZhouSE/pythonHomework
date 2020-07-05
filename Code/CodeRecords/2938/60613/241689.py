lst=[i for i in range(1,101)]
lst=list(map(str,lst))
lst.sort()
for i in range(100):
    print(lst[i])