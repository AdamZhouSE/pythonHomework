def main():
    numOftests = int(input())
    for i in range(numOftests):
        n = int(input())
        if divisorSum(n)<2*n:
            print(1)
        else:print(0)

def divisorSum(num):
    sum = 0
    for i in range(1,num+1):
        if num%i == 0:
            sum+=i
    return sum

if __name__ == '__main__':
    main()


