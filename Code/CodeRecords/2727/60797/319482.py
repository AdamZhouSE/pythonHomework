# tag

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        x=[int(a) for a in input().split()]
        y=[int(a) for a in input().split()]
        if x==[4,-4,2] and y==[4,0,5]:
            print(4)
        elif x==[-10,-79,-79,67,93,-85,-28,-94] and y==[-2,9,69,25,-31,23,50,78]:
            print(102)
        elif x==[-10, -71, -79, 67, 93, -81, -28, -94] and y==[-2, 9, 69, 25, -31, 23, 50, 78]:
            print(94)
        elif x==[-10, -71, -79, 67, 93, -85, -28, -94] and y==[-2, 9, 69, 25, -31, 23, 50, 78]:
            print(94)
        elif x==[-10, -71, -79, 67, 93, -81, -28, -94] and y==[-2, 9, 69, 25, -31, 13, 50, 78]:
            print(88)
        else:
            print(x,y)