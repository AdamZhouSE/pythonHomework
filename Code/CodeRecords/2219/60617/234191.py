import math
def main():
    c=int(input())
    Csqrt=int(math.sqrt(c))
    for a in range(Csqrt+1):
        for b in range(Csqrt+1):
            if (a*a+b*b)==c:
                print(True)
                exit()
    print(False)
if __name__  =='__main__':
    main()