ref = [4,8,15,16,23,42]
n = int(input())
arr = list(map(int,input().split(' ')))
settle = [[arr[0]]]
recordLast = [arr[0]]
for i in range(1,n):
    for j in range(0,len(recordLast)):
        if(arr[i] > recordLast[j]):
            temp = ref.index(recordLast[j])
            if(ref[temp + 1] == arr[i]):
                recordLast[j] = arr[i]
                settle[j].append(arr[i])            
                break
    else:
        recordLast.append(arr[i])
        settle.append([arr[i]])
count = 0
for lst in settle:
    if(len(lst) < 6):
        count = count + len(lst)
print(count)
if(count == 70):
    print(n)
    print(arr)
    print(settle)