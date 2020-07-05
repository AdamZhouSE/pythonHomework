def nums_23_Smallest(num):
    k = 2
    while(True):
        i = 0
        co = 0
        while(co<num):
            co+=pow(k,i)
            i+=1
        if co == num:
            break
        else:
            k += 1
    print(k)
if __name__=='__main__':
    n = int(input())
    nums_23_Smallest(n)