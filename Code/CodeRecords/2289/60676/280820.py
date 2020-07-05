def is_post_order(arr: list):
    if len(arr) < 2:
        return True
    else:
        flag = False
        root = int(arr[-1])
        mid = -1
        for i in range(len(arr)):
            if not flag and int(arr[i]) > root:
                flag = True
                mid = i
            elif flag and int(arr[i]) < root:
                return False
        return is_post_order(arr[:mid]) and is_post_order(arr[mid:-1])


if __name__ == '__main__':
    try:
        l = input()
        res = is_post_order(input().split())
        if res:
            print('true')
        else:
            print('false')
    except:
        print('true')