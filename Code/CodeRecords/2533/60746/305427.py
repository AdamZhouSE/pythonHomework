N=list(input())
def sort(A):
    newArray=[]
    for i in A:
        if i.isdecimal():
            if int(i)%2==0:
                newArray.append(int(i))
    for i in A:
        if i.isdecimal():
            if int(i)%2!=0:
                newArray.append(int(i))
    return newArray
print(sort(N))