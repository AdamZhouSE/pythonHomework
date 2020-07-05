def main():
    numOftests = int(input())
    for i in range(numOftests):
        list0 = input().split()
        s = list0[0]
        sum0 = 0
        list1 = []
        for j in range(1,len(s)+1):
            for k in range(0,len(s)-j+1):
                    list1.append(s[k:k+j])
        cnt = 0
        k = int(list0[1])
        for x in list1:
            if func(x,k):
                cnt+=1
        print(cnt)

def func(str0,k):
    cnt = 0;
    for x in str0:
        if x=="1":
            cnt+=1
    if cnt==k:
        return True
    else:return False

if __name__ == '__main__':
    main()