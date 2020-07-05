def noEmpty(s:str):
    return s and s.strip() and s!="null"

arr1=list(filter(noEmpty,input()[1:-1].split(",")))
arr2=list(filter(noEmpty,input()[1:-1].split(",")))
arr1.extend(arr2)
arr1=list(map(int,arr1))
arr1.sort()
print(arr1)