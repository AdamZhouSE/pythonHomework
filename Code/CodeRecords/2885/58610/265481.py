for _ in range(eval(input())):
    n = eval(input())
    mod_res = [0, 0, 0]
    for num in list(map(int, input().split(' '))):
        mod_res[num % 3] += 1
    t = min(mod_res[1], mod_res[2])
    print(mod_res[0] + t + (mod_res[1] + mod_res[2] - 2 * t) // 3)