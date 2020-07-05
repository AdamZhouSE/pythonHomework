t = int(input())
while t:
    b = int(input())
    blocks = [int(n) for n in input().split( )]
    index = 0
    v = 0
    if b<3:
        print('0')
    else:
        while index<b-2:
            if blocks[index]<=blocks[index+1]:
                index += 1
            else:
                test = index+1
                bool = True
                while test<b-1 and bool:
                    if blocks[test]>=blocks[test+1]:
                        test += 1
                    else:
                        right = test+1
                        bool = False
                bool = True
                while right<b-1 and bool:
                    if blocks[right]<=blocks[right+1]:
                        right += 1
                    else:
                        bool = False
                sub = blocks[index:right]
                height = min(blocks[index], blocks[right])
                for i in range(1, len(sub)):
                    v += height - blocks[index+i]
                index = right
    print(v)
    t -= 1
    