def judge(a,index):
    if a[index] == None:
        return True
    if index*2+1 >= len(a):
        return True
    left_index = index*2+1
    right_index = index*2+2
    if a[left_index] == None:
        left_index = index
    else:
        while left_index*2+2 < len(a) and a[left_index*2+1] != None:
            left_index = left_index*2+2
    if a[left_index] == None:
        left_index = index
    else:
        while right_index*2+1 < len(a) and a[right_index*2+2] != None:
            right_index = right_index*2+1
    
    if a[index] >= a[left_index] and a[index] <= a[right_index] and judge(a,index*2+1) and judge(a,index*2+2):
        return True
    else:
        return False
null = None
a = eval(input())
temp = 0
if judge(a,0):
    print('true')
else:
    print('false')
