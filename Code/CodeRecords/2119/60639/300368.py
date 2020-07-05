num=list(map(int,input().split(',')))
if (num[0]>=num[2] or num[1]>=num[3]) and num[0]+num[1]<=num[2]+num[3]:
    print(True)
else:
    print(False)