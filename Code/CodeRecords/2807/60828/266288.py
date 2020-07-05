def h24():
    n,m = map(int,input().split())
    box = list(map(int,input().split()))
    key = list(map(int,input().split()))
    num_box_even = 0
    num_key_even = 0
    for i in range(n):
        if(box[i]%2==0):
            num_box_even += 1
    for i in range(m):
        if(key[i]%2==0):
            num_key_even += 1
    num_box_odd = n - num_box_even
    num_key_odd = m - num_key_even
    res = min(num_key_even,num_box_odd) + min(num_box_even,num_key_odd)
    print(res)

if __name__ == '__main__':
    h24()