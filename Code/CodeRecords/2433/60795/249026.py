def list(arr):
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
                re.append(arr[i])
        else:
            re.append(arr[i])
    return re