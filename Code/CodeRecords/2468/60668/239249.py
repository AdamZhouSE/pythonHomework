def arrays_9_multArray():
    T = int(input())
    try:
        while T>0:
            list_mul = []
            n = input()
            list = [int(i) for i in input().split()]
            for i in range(0,len(list)):
                num = 1
                for j in range(0,i):
                    num *= list[j]
                for k in range(i+1,len(list)):
                    num *= list[k]
                list_mul.append(num)
            for i in range(0,len(list_mul)-1):
                print(list_mul[i],end=' ')
            print(list_mul[len(list_mul)-1],end=' ')
            print("")
            T-=1
    except EOFError:
        pass
if __name__ == '__main__':
    arrays_9_multArray()