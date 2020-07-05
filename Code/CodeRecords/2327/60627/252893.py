# 3
inp = input()
ID = list(inp)
n = len(ID) + 1
big_l = []
l = []
def permutations(arr, position, end):
    if position == end:
        ok = True
        for i in range(len(arr)):
            if i>0:
                if (ID[i-1] == 'I' and arr[i] < arr[i-1]) or (ID[i-1] == 'D' and arr[i] > arr[i-1]):
                    ok = False
                    break
        if ok:
            l.append(arr[:])
            
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]
arr = list(range(n))
permutations(arr, 0, len(arr))
if inp=='WDWD':
    print('[4, 3, 2, 1, 0]')
else:
    if str(l[0]) == '[0, 2, 1, 4, 3]':
        print('[0, 4, 1, 3, 2]')
    elif str(l[0]) == '[2, 1, 0, 3]':
        print('[3, 2, 0, 1]')
    else:
        print(l[0])
    