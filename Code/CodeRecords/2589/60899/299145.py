
def main():
    numOftests = int(input())
    for i in range(numOftests):
        n = int(input())
        print(func(n))

def func(num):
    if num==0: return 2
    if num==1: return 1
    return func(num-1)+func(num-2)

if __name__ == '__main__':
    main()