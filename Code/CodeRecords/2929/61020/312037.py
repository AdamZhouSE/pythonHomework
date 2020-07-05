import typing

n_m: typing.List[str] = input().split()
n: int = int(n_m[0])
m: int = int(n_m[1])

as_and_bs: typing.List[typing.Tuple[int, int]] = []
for i in range(n):
    a_and_b = input().split()
    as_and_bs.append((int(a_and_b[0]), int(a_and_b[1])))

a_sum = 0
for a_b in as_and_bs:
    a_sum += a_b[0]

target = a_sum - m
if target <= 0:
    print('0')
else:
    as_and_bs.sort(key=lambda x: x[0] - x[1], reverse=True)
    compress_num = 0
    num_of_comp_songs = 0
    for a_b in as_and_bs:
        num_of_comp_songs += 1;
        compress_num += a_b[0] - a_b[1]
        if compress_num >= target:
            break

    else:
        num_of_comp_songs = -1

    print(num_of_comp_songs)
