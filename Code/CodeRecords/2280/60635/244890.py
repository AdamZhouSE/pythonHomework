count=int(input())
for n in range(count):
    num=int(input())-1
    array = [int(x) for x in input().split()]
    curr=1
    for a in array:
        if a>curr:
            print(curr)
            break
        curr += 1
    
    