def getSecond(arr):
    return(arr[1])
def veganFilter(num,arr):
    i=0
    while i<len(arr):
        if arr[i][2]<num:
            del arr[i]
        else:
            i+=1
    return(arr)
def priceFilter(num,arr):
    i = 0
    while i < len(arr):
        if arr[i][3] > num:
            del arr[i]
        else:
            i += 1
    return (arr)
def distanceFilter(num,arr):
    i = 0
    while i < len(arr):
        if arr[i][4] > num:
            del arr[i]
        else:
            i += 1
    return (arr)
def rate(arr):
    arr.sort(key=getSecond,reverse=True)
    for i in range(len(arr)-1):
        if arr[i][1]==arr[i+1][1] and arr[i][0]<arr[i+1][0]:
            temp=arr[i+1]
            arr[i+1]=arr[i]
            arr[i]=temp
        else:
            continue
    return(arr)

restaurants=eval(input())
veganStandard=int(input())
restaurants=veganFilter(veganStandard,restaurants)
priceStandard=int(input())
restaurants=priceFilter(priceStandard,restaurants)
distanceStandard=int(input())
restaurants=distanceFilter(distanceStandard,restaurants)
restaurants=rate(restaurants)
result=[]
for i in range(len(restaurants)):
    result.append(restaurants[i][0])
print(result,end='\n')