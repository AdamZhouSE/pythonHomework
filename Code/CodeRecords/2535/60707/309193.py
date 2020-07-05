
def maxChunksToSorted(arr):

    """

    :type arr: List[int]

    :rtype: int

    """

    res=0

    n=len(arr)

    tmp=arr.copy()

    tmp.sort()

    max_val=0

    for i in range(n):

        if arr[i]>max_val:

            max_val=arr[i]

        if i==n-1:

            res+=1

        else:

            if tmp[i]==max_val and min(arr[i+1:])>=max_val:

                res+=1

                max_val=0

    return res




if __name__ == "__main__":
    inp1 = input().split("[")
    temp1 = inp1[1].split("]")
    temp2 = temp1[0].split(",")
    for i in range(len(temp2)):
        temp2[i] = int(temp2[i])
    r1 = maxChunksToSorted(temp2)
    print(r1)