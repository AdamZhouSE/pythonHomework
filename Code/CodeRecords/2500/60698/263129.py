#19
def test(arr):
    result=[]
    cookie_sort(arr,result)
    return result


def cookie_sort(arr,result):
    max_index = arr.index(max(arr))
    arr_copy=list(arr)
    if max_index!=len(arr_copy)-1:
        if max_index!=0:
            arr_copy = list(reversed(arr_copy[0:max_index + 1])) + arr_copy[max_index + 1:len(arr_copy)]
            result.append(max_index + 1)
        arr_copy = list(reversed(arr_copy))
        result.append(len(arr_copy))
    if len(arr_copy)<=2:
        return
    cookie_sort(arr_copy[0:len(arr_copy)-1],result)

if __name__ == '__main__':
    arr=list(eval(input()))
    operation=test(arr)
    print(operation)
    
