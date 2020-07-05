def move_times(lst):
    lst=sorted(lst)
    if lst[0]+1==lst[1] and lst[1]+1==lst[2]:
        return [0,0]
    else:
        max_times=lst[2]-lst[0]-2
        pre=lst[1]-lst[0]
        lat=lst[2]-lst[1]
        if pre==1 or lat==1:#有两个石子是靠一起的
            min_t=1
        elif pre==2 or lat==2:#有两个石子中间空了一个 另外一个可以插进去
            min_t=1
        else:
            min_t=2
        return [min_t,max_times]


if __name__=="__main__":
    a=eval(input())
    b=eval(input())
    c=eval(input())
    lst=[a,b,c]
    ans=move_times(lst)
    print(ans)