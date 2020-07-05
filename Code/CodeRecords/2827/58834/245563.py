n = int(input())
boxes_origion = input()
boxes = boxes_origion.split()


#排序函数
def subsequence(m):
    lenth = len(m)
    for number in range(0,lenth):
        for d in range(number+1,lenth):
            if int(m[number]) > int(m[d]):
                i = m[number]
                m[number] = m[d]
                m[d] = i
            else:
                 continue


subsequence(boxes)
print(" ".join(i for i in boxes))
