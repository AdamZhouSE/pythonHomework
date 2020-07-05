def change(num, time):
    if num==1:
        return time
    elif num%2==0:
        return change(num/2,time+1)
    else:
        return min( change(num+1,time+1) , change(num-1,time+1) )



if __name__ == '__main__':
    n=int(input())
    print(change(n,0))