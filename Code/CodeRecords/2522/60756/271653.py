arr1=list(map(int,input()[1:-1].split(",")))
arr2=list(map(int,input()[1:-1].split(",")))
def compare(x:int):
    if x in arr2:
        return arr2.index(x)
    else:
        return len(arr2)+x
arr1.sort(key=compare)
print(arr1)