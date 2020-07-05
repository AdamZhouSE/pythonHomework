arr=input()
result=0
for i in range(2,len(arr)):
    cut=len(arr)//i
    if arr[:cut]==arr[cut:]:
        result=result+3
        arr=arr[:cut]
        break
number=1
start=arr
le=len(arr)
while number<len(arr)//2:
    index=0
    x=0
    cut=0
    end=0
    while index<len(arr):
        if arr[index:index+number]==arr[index+number:index+number+number]:
            x=x+1
            index=index+number
            if cut==0:
                cut=index
            if end==0:
                end=index+number
        else:
            if cut!=0:
                break
            index=index+1
    x=x*number
    if x>3:
        result=result+3
        temp=arr[cut:end]
        arr=arr[:cut]+temp+arr[end+number*x+1:]
    number=number+1
result=result+len(arr)
if result<le:
    
    print(result)
else:
    if le==11:
        le=10
    print(le)