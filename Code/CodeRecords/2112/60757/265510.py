arr=list(eval(input()))
for i in range(len(arr)+1):
    if arr.count(i)==0:
        print(i)
        break