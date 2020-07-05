def recursion(index,angle):
    if index==n:
        return True if angle%360==0 else False
    return recursion(index+1,angle+arr[index+1]) or recursion(index+1,angle-arr[index+1])


if __name__ == '__main__':
    n=int(input())
    arr=[]
    arr.append(None)
    for i in range(0,n):
        temp=int(input())
        arr.append(temp)
    if recursion(0,0):
        print("YES")
    else:
        print("NO")