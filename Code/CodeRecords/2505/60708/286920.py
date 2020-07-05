def find(list,n):
    list=sorted(list)
    for i in range(0,n-1):
        if list[i+1]==list[i]:
            return list[i]
    return 0
if __name__ == '__main__':
    temp=input().split(",")
    print(find(temp,len(temp)))
