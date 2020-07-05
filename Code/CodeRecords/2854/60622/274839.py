arr=list(map(int,input().split()))
if len(set(arr))>3:
    print("Alien")
elif  len(set(arr))==3:
    print("Bear")
else:
    print("Elephant")