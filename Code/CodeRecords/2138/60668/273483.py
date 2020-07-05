def nums_25_Sum(k,list=[]):
    co = False
    for i in range(len(list)):
        if list[i]<k and i != len(list)-1:
            for j in range(i+1,len(list)):
                if (list[i] + list[j])%k==0:
                    co = True
    print(co)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    k = int(input())
    nums_25_Sum(k,list)