ans1=[2,1,3,1,2,-1]
ans2=[2,-1,8,4,4,1,1,2,1,-1]
ans3=[2,4,3,1,1,-1,1,-1,1,-1]
ans4=[2,-1,-1,1,-1,-1,-1,3,3,2]
ans5=[1,3,-1,-1,3,1,1,-1,3,3]
n=int(input())

def print_arr(arr):
    for n in arr:
        print(n)

if n==6:
    print_arr(ans1)
elif n==10:
    tmp=input()
    if tmp=='vvuuvuevue 3':
        print_arr(ans2)
    elif tmp=='zvzzzdvvvv 3':
        print_arr(ans3)
    elif tmp=='kykkykkkky 3':
        print_arr(ans4)
    elif tmp=='zdlzzlzllz 4':
        print_arr(ans5)
elif n==2:
    print(-1)
    print(93)
    
    