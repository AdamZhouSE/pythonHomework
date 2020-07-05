def find(list):
    for i,j in enumerate(list):
        n=len(list)-j
        if(list[n-1]<=j and list[n]>=j):
            return j
if __name__ == '__main__':
    temp=input()
    for i,j in enumerate(temp):
        if j=='[':
            break
    list=eval(temp[i:len(temp)])
    print(find(list))