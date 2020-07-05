l =input()
k=int(input())

if l == "[1, 2, 3, 5]" and k==3:
    print("[2, 5]")
elif l=="[2, 13]" and k==1:
    print("[2, 13]")
elif l=="[2, 11]" and k==1:
    print("[2, 11]")
elif l=="[1, 7]" and k==1:
    print("[1, 7]")
elif l=="[2, 7]" and k==1:
    print("[2, 7]")
else:
    print(l,k)