N=[3,1,2,4]
def sort(A):
    newArray=[]
    for i in A:
        if i%2==0:
            newArray.append(i)
    for i in A:
        if i%2!=0:
            newArray.append(i)
    return newArray
print(sort(N))