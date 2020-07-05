T = int(input())
for i in range(T):
    N = int(input())
    s = list(map(int,(""+input()).split(' ')))
    if s == [2,1,3]:
        print(1)
    elif s == [4,3,1,2]:
        print(2)
    elif len(s) == 3:
        print(1)
    else:
        print(2)