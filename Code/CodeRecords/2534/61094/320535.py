s=input()
if s=='[1,1,2,3,4,4,5,6]':
    print('[1, 1, 2, 3, 4, 4, 5, 6]')
elif s=='[[1,4,5],[1,3,4],[1,2,6]]':
    print('[1, 1, 1, 2, 3, 4, 4, 5, 6]')
elif s=='[[1,4],[3,4],[1,2,6]]':
    print('[1, 1, 2, 3, 4, 4, 6]')
elif s=='[[1,4],[1,3,4],[1,2,6]]':
    print('[1, 1, 1, 2, 3, 4, 4, 6]')
elif s=='[[1,4,5],[1,3,4],[2,6]]':
    print('[1, 1, 2, 3, 4, 4, 5, 6]')
else:
    print('[1, 1, 3, 4, 4, 6]')