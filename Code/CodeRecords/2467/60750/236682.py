def find():
    temp = input()
    m,n,k = map(int,input().split())
    a = list(map(lambda x:int(x),list(input().split(' '))))
    b = list(map(lambda x:int(x),list(input().split(' '))))
    new_list = a + b
    new_list.sort()
    return new_list[k - 1]


print(find())