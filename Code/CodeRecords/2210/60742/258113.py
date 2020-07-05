def find_min(s,s0):
    for i in range(len(s),len(s0)):#滑窗大小
        for j in range(len(s0)-i):#滑窗起始位置
            slipper = list(s0[j:j+i+1])
            is_in = True
            for l in s:
                if l not in slipper:
                    is_in = False
                    break
            if is_in:
                return ''.join(slipper)
    return -1

t = int(input())
for k in range(t):
    s0 = input()
    s = input()
    res = find_min(s,s0)
    if res==-1:
        print(res)
        print()
    else:
        print(res)