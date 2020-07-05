n = int(input())
board =[[]*n]*n
for i in range(n):
    board[i]=list(input())
bl = False
for i in range(n):
    bl = True
    for j in range(n):
        up = i-1
        down = i+1
        left = j-1
        right = j+1
        num = 0
        if up>0:
            if board[up]=="o":
                num+=1
        if down<n:
            if board[down]=="o":
                num+=1
        if left>0:
            if board[left]=="o":
                num+=1
        if right<n:
            if board[right]=="o":
                num+=1
        if num%2!=0:
            bl = False
            break
    if bl == Fasle:
        break
print("YES" if bl else "NO")
      
            