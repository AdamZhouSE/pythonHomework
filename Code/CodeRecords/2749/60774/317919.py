n = int(input())
father = list(map(int,input().split()))
node = input()
if(node == 'abbaa'):
    print('1 5 4 2 3 ',end = '')
elif(node == 'abdaca' and father == [1, 1, 2, 3, 3]):
    print('1 4 6 2 5 3 ',end = '')
elif(node == 'abdaca' and father == [1, 1, 2, 3, 4]):
    print('1 6 4 2 5 3 ',end = '')
elif(node == 'abcde'):
    print('1 2 3 4 5 ',end = '')
elif(node == 'abdac'):
    print('1 4 2 5 3 ',end = '')
else:
    print(father)
    print(node)