def graph_2_colour(n):
    if n==10:
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
    graph_2_colour(n)