a=list(map(int,input().split()))
a.remove(0)
a.reverse()
print(" ".join(str(i) for i in a),end=" ")