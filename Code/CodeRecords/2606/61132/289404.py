def find(l,k):
    try:
        return l.index(k)
    except Exception as e:
        return -1


l=eval(input())
k=int(input())
print(find(l,k))