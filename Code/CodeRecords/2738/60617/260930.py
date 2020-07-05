def largestRectangle(arr):
    for i in range(0, len(arr[0])):
        height=0
        for j in range(0, len(arr)):
            if arr[j][i]!='0':
                height+=1
            else:
                height=0
            arr[j][i]=height
    maxArea=0
    for row in arr:
        temp=largestRectangleArea(row)
        if temp>maxArea:
            maxArea=temp
    print(maxArea)

def largestRectangleArea(arr):
    stack=[]
    i=0
    maxArea=0
    # if arr==[3, 1, 3, 2, 2]:
    #     print("success")
    while i<len(arr):

        if not stack or arr[i]>arr[stack[-1]]:
            stack.append(i)
            i+=1
        else:
            k=stack.pop()
            temp=arr[k]*((i-stack[-1]-1) if stack else i)
            maxArea=max(temp,maxArea)
    while stack:
        k=stack.pop()
        maxArea=max(maxArea, arr[k]*((i-stack[-1]-1) if stack else i))
    return maxArea




if __name__=='__main__':
    arr=[]
    while True:
        try:
            arr.append(input())
        except:
            break
    arr.remove("[")
    arr.remove("]")
    arr="".join(arr)
    arr=eval("["+arr+"]")
    largestRectangle(arr)
    print(arr)


