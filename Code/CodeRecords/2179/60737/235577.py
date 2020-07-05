def get_height(a, b):
    lista = list(a)
    listb = list(b)
    length = min(len(lista), len(listb))
    count = 0
    for i in range(0, length):
        if lista[i] == listb[i]:
            count += 1
        else:
            break
    return count


if __name__ == "__main__":
    con = input()
    m = int(con.split( )[1])
    s = input()
    while m > 0:
        nums = input().split( )
        s1 = s[int(nums[0])-1 : int(nums[1])]
        s2 = s[int(nums[2])-1 : int(nums[3])]
        print(get_height(s1, s2))
        m -= 1
