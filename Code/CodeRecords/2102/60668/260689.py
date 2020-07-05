import math


def nums_8_Count(n):
    re = []
    for i in range(2,n):
        co = 0
        for j in range(1,int(math.sqrt(i))+1):
            if i%j==0:
                co+=1
        if co ==1:
            re.append(i)
    print(len(re))
if __name__=='__main__':
    n = int(input())
    nums_8_Count(n)