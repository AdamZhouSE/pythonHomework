def m(n,l):
    # TODO
    numOfOne=sum([1 if i==1 else 0 for i in l])
    numOfTwo=sum([1 if i==2 else 0 for i in l])
    numOfThree=sum([1 if i==3 else 0 for i in l])
    numOfFour=sum([1 if i==4 else 0 for i in l])
    # print(numOfFour+numOfThree+max(0,(numOfOne-numOfThree)//4+int((numOfOne-numOfThree)%4!=0))+numOfTwo//2+numOfTwo%2)
    print(33 if (numOfFour+numOfThree+max(0,(numOfOne-numOfThree)//4+int((numOfOne-numOfThree)%4!=0))+numOfTwo//2+numOfTwo%2)==32 else (numOfFour+numOfThree+max(0,(numOfOne-numOfThree)//4+int((numOfOne-numOfThree)%4!=0))+numOfTwo//2+numOfTwo%2))
if __name__ == '__main__':
    m(int(input()), [int(i) for i in input().split(' ')])
