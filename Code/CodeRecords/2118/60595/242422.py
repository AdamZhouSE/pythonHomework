import math
def Test():
    try:
        num=int(input())
        a=math.log(num,3)
        print(int(a)==a)
    except:
        print(False)

if __name__ == "__main__":
    Test()