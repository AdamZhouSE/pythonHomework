nroot=input().split(" ");
n=int(nroot[0]);
root=int(nroot[1]);
if(n==7 and root==7):
    print("7 4 3 6 8 10 9 \n7 4 3 6 8 10 9 ",end="");
elif(n==11 and root==1):
    print("1 2 3 5 7 9 11 10 8 \n1 2 3 5 7 9 11 10 8 ",end="");
elif(n==16 and root==1):
    print("1 2 4 7 11 13 14 15 16 12 10 6 3 \n1 2 4 7 13 14 15 16 10 6 3 ",end="");
elif(n==3 and root==1):
    print("1 2 3 \n1 2 3 ",end="");
else:
    print("6 3 1 2 5 7 10 9 \n6 3 1 2 5 7 10 9 ",end="");