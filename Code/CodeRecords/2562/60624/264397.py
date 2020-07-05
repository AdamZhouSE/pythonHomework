def func1():
    a = int(input())
    while a > 0:
        a -= 1
        temp = list(map(int, input().split(" ")))
        N = temp[0]
        Q = temp[1]
        temp = list(map(int, input().split(" ")))
        unread, read, trash = list(range(1,N+1)), [], []
        for i in range(0,len(temp),2):
            if temp[i]==1:
                read.append(temp[i+1])
                unread.remove(temp[i+1])
            elif temp[i]==2:
                trash.append(temp[i+1])
                read.remove(temp[i+1])
            elif temp[i]==3:
                trash.append(temp[i+1])
                unread.remove(temp[i+1])
            else:
                read.append(temp[i+1])
                trash.remove(temp[i+1])
        def helper(li):
            if len(li)==0:
                print("EMPTY")
            else:
                for i in li:
                    print(i,end=" ")
            print()
        helper(unread)
        helper(read)
        helper(trash)
    return
func1()