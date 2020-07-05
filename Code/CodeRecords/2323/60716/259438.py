strs = input().split(',')
lists = [int(i) for i in strs]
k = int(input())
lists.sort()
if k==0:
    print(lists[len(lists)-1]-lists[0])
else:
    a = lists[0]
    b = lists[len(lists)-1]
    if a+k>=b-k:
        print(0)
    else:
        print(b-k-a-k)