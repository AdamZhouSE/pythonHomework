try:
    s1=input()
    arr1=s1[1:len(s1)-1].split(',')
    if 'null' in arr1:
        arr1.remove('null')
    s2=input()
    
    arr2=s2[1:len(s2)-1].split(',')
    if 'null' in arr2:
        arr2.remove('null')
    if '' in arr1:
        arr1.remove('')
    if '' in arr2:
        arr2.remove('')
    arr1=list(map(int,arr1))
    arr2=list(map(int,arr2))
    print(sorted(arr1+arr2))
except Error:
    pass