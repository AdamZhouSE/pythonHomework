def rev_num():
    num=input()
    if num[0]=='-':
        temp=reversed(num[1:])
        while temp[0]=='0':
            temp=temp[1:]
        print('-'+temp,end="")
    else:
        temp=reversed(num)
        while temp[0]=='0':
            temp=temp[1:]
            print(temp,end="")
            
if __name__=='__main__':
    rev_num()