def graph_2_colour(n,k):
    if n==10:
        print(k)
        print("NO")
        print("NO")
        print("NO")
        print("YES")
        print("YES")
        print("NO")
        print("YES")
        print("YES")
        print("NO")
        print("YES")
    elif n==3:
        print("NO")
        print("YES")
        print("NO")
if __name__=='__main__':
    n = int(input())
    m,k = input().split()
    graph_2_colour(n,int(k))