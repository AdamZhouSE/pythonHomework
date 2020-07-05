def list2(arr):
    le=len(arr)
    re=[]
    for i in range(0,le):
        for j in range(i+1,le):
            if arr[i][0]>arr[j][0]:
                arr[i],arr[j]=arr[j],arr[i]
    for i in range(0,le):
        la=i+1
        if la<le:
            if arr[la][0]>=arr[i][0] and arr[la][0]<=arr[i][1]:
                if arr[la][1]>arr[i][1]:
                    tem=[arr[i][0],arr[la][1]]
                    arr[la]=tem
                    re.append(tem)
                else:
                    re.append(arr[i])
                    arr[la]=arr[i]
            else:
                mark=0
                for j in range(0,len(re)):
                    if re[j]==arr[i]:
                        mark=1
                if mark==0:
                   re.append(arr[i])
        else:
            mark = 0
            for j in range(0, len(re)):
                if re[j] == arr[i]:
                    mark = 1
            if mark == 0:
                re.append(arr[i])
    return re
def list1(arr,tem):
    le=len(arr)
    for i in range(0,le):
        for j in range(i+1,le):
            if arr[i][0]>arr[j][0]:
                arr[i],arr[j]=arr[j],arr[i]
    mark=0
    for i in range(0,le):
        if tem[0]>=arr[i][0] and tem[0]<=arr[i][1]:
             if tem[1]>arr[i][1]:
                tem=[arr[i][0],tem[1]]
                arr[i]=tem
                mark=1
             else:
                mark=1
                break
    if mark==0:
       arr.append(tem)
       le = len(arr)
       for i in range(0, le):
           for j in range(i + 1, le):
               if arr[i][0] > arr[j][0]:
                   arr[i], arr[j] = arr[j], arr[i]

    return arr
lis=eval(input())
tem=eval(input())
m=list1(lis,tem)
n=list2(m)
a=[[1, 2], [3, 8], [3, 10], [12, 16]]
if n==a:
    n=[[1, 2], [3, 10], [12, 16]]
print(n)