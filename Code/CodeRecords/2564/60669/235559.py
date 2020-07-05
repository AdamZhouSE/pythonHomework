list=eval(input())
k=int(input())
x=int(input())
diff=[]
result=[]

for item in list:
    diff.append(abs(item-x))
diff.sort()

for i in range(0,k):   #(0,k-1)
    try:
        index=list.index(x-diff[i])
    except:
        index=list.index(x+diff[i])
    result.append(list[index])
    list.pop(index)
result.sort()
print(result)