def findMaxGap():
    li=list(map(int, eval(input())))
    li.sort()
    if len(li)<2:
        print(0)
        exit()
    else:
        maxGap=0
        for i in range(0, len(li)-1):
            if li[i+1]-li[i]>maxGap:
                maxGap=li[i+1]-li[i]
    print(maxGap)
    
if __name__=='__main__':
    findMaxGap()