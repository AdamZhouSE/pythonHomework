import math

def pigNum(buckets,minutesToDie,minutesToTest):
    k = int(minutesToTest / minutesToDie) + 1
    ans = math.ceil(math.log( buckets, k))
    return ans

if __name__ == '__main__':
    buckets = int(input())
    minutesToDie = int(input())
    minutesToTest = int(input())
    print(pigNum(buckets,minutesToDie,minutesToTest))