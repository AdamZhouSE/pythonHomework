arr=(sorted(eval(input())))
for i in range(1,len(arr)+2):
    if arr.count(i)==0:
        print(i)
        break