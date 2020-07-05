def find(temp,left,right):
    if left==right:
        print(temp[left])
        return temp[left]
    mid=int((left+right)/2)
    flag=bool((mid+1)%2==0)#奇偶性 按理说奇数与后面相等 偶数与前面相等
    if flag:
        if temp[mid]==temp[mid-1]:
            left=mid
            find(temp,left,right)
        elif temp[mid]==temp[mid+1]:
            right=mid
            find(temp,left,right)
        else:
            print(temp[mid])
            return temp[mid]
    else:
        if temp[mid]==temp[mid-1]:
            right=mid
            find(temp,left,right)
        elif temp[mid]==temp[mid+1]:
            left=mid
            find(temp,left,right)
        else:
            print(temp[mid])
            return temp[mid]
def stringToArray(string):
    string=string[1:len(string)-1]
    array=string.split(",")
    return array
temp=stringToArray(input())
left=0
right=len(temp)
find(temp,left,right)